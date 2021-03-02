import os
from functools import partial

from core.utils import colors

end_color = colors.END

def clear_screen() -> None:
    os.system("clear")


def empty_lines(n: int) -> None:
    print("\n" * (n-1))


def _make_colored(text, color: str, *, end: bool = True) -> str:
    if end:
        return f"{color}{text}{colors.END}"
    else:
        return f"{color}{text}"


red = partial(_make_colored, color=colors.RED)
green = partial(_make_colored, color=colors.GREEN)
blue = partial(_make_colored, color=colors.BLUE)

arrow = blue("└──>")
