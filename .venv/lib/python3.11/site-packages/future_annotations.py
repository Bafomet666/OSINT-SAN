import argparse
import ast
import codecs
import encodings
import io
import sys
import tokenize
import warnings
from typing import Match
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple

import tokenize_rt


def _ast_parse(contents_text: str) -> ast.Module:
    # intentionally ignore warnings, we might be fixing warning-ridden syntax
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        return ast.parse(contents_text.encode())


def _ast_to_offset(node: ast.expr) -> tokenize_rt.Offset:
    return tokenize_rt.Offset(node.lineno, node.col_offset)


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.offsets: Set[tokenize_rt.Offset] = set()

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        self.offsets.add(_ast_to_offset(node.annotation))
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        args = []
        if hasattr(node.args, 'posonlyargs'):  # pragma: no cover (py38+)
            args.extend(node.args.posonlyargs)
        args.extend(node.args.args)
        if node.args.vararg is not None:
            args.append(node.args.vararg)
        args.extend(node.args.kwonlyargs)
        if node.args.kwarg is not None:
            args.append(node.args.kwarg)

        for arg in args:
            if arg.annotation is not None:
                self.offsets.add(_ast_to_offset(arg.annotation))

        if node.returns is not None:
            self.offsets.add(_ast_to_offset(node.returns))

        self.generic_visit(node)


utf_8 = encodings.search_function('utf8')


def _new_coding_cookie(match: Match[str]) -> str:
    s = match[0]
    i = 0
    while s[i].isspace():
        i += 1
    ret = f'{s[:i]}# {"*" * (len(s) - 2 - i)}'
    assert len(ret) == len(s), (len(ret), len(s))
    return ret


def decode(b: bytes, errors: str = 'strict') -> Tuple[str, int]:
    u, length = utf_8.decode(b, errors)

    # replace encoding cookie so there isn't a recursion problem
    lines = u.splitlines(True)
    for idx in (0, 1):
        if idx >= len(lines):
            break
        lines[idx] = tokenize.cookie_re.sub(_new_coding_cookie, lines[idx])
    u = ''.join(lines)

    visitor = Visitor()
    visitor.visit(_ast_parse(u))

    tokens = tokenize_rt.src_to_tokens(u)
    for i, token in tokenize_rt.reversed_enumerate(tokens):
        if token.offset in visitor.offsets:
            # look forward for a `:`, `,`, `=`, ')'
            depth = 0
            j = i + 1
            while depth or tokens[j].src not in {':', ',', '=', ')', '\n'}:
                if tokens[j].src in {'(', '{', '['}:
                    depth += 1
                elif tokens[j].src in {')', '}', ']'}:
                    depth -= 1
                j += 1
            j -= 1

            # look backward to delete whitespace / comments / etc.
            while tokens[j].name in tokenize_rt.NON_CODING_TOKENS:
                j -= 1

            quoted = repr(tokenize_rt.tokens_to_src(tokens[i:j + 1]))
            tokens[i:j + 1] = [tokenize_rt.Token('STRING', quoted)]

    return tokenize_rt.tokens_to_src(tokens), length


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    def _buffer_decode(self, input, errors, final):  # pragma: no cover
        if final:
            return decode(input, errors)
        else:
            return '', 0


class StreamReader(utf_8.streamreader):
    """decode is deferred to support better error messages"""
    _stream = None
    _decoded = False

    @property
    def stream(self):
        if not self._decoded:
            text, _ = decode(self._stream.read())
            self._stream = io.BytesIO(text.encode('UTF-8'))
            self._decoded = True
        return self._stream

    @stream.setter
    def stream(self, stream):
        self._stream = stream
        self._decoded = False


# codec api

codec_map = {
    name: codecs.CodecInfo(
        name=name,
        encode=utf_8.encode,
        decode=decode,
        incrementalencoder=utf_8.incrementalencoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=utf_8.streamwriter,
    )
    for name in ('future-annotations', 'future_annotations')
}


def register() -> None:  # pragma: no cover
    codecs.register(codec_map.get)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description='Prints transformed source.')
    parser.add_argument('filename')
    args = parser.parse_args(argv)

    with open(args.filename, 'rb') as f:
        text, _ = decode(f.read())
    getattr(sys.stdout, 'buffer', sys.stdout).write(text.encode('UTF-8'))
    return 0


if __name__ == '__main__':
    exit(main())
