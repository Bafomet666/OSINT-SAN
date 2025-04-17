"""Censys search CLI."""

import argparse
import json
import sys
import webbrowser
from pathlib import Path
from typing import Any, Dict, List
from urllib.parse import urlencode

from censys.cli.utils import V2_INDEXES, err_console, write_file
from censys.common.exceptions import CensysCLIException
from censys.search import SearchClient
from censys.search.v2.api import CensysSearchAPIv2

Results = List[dict]

DATA_DIR = Path(__file__).parent.parent / "data"
HOSTS_AUTOCOMPLETE = DATA_DIR / "hosts_autocomplete.json"
CERTIFICATES_AUTOCOMPLETE = DATA_DIR / "certificates_autocomplete.json"


def fields_completer(
    prefix: str, parsed_args: argparse.Namespace, **kwargs
) -> List[str]:
    """Fields completer.

    Args:
        prefix (str): Prefix to complete.
        parsed_args (Namespace): Argparse Namespace.
        **kwargs: Keyword arguments.

    Returns:
        List[str]: List of fields.
    """
    index_type = parsed_args.index_type
    autocomplete_json = {}
    if index_type == "hosts":
        with HOSTS_AUTOCOMPLETE.open() as autocomplete_file:
            autocomplete_json = json.load(autocomplete_file)
    elif index_type == "certificates":
        with CERTIFICATES_AUTOCOMPLETE.open() as autocomplete_file:
            autocomplete_json = json.load(autocomplete_file)
    else:
        return []

    autocomplete_data = autocomplete_json.get("data", [])
    fields = [
        field_value
        for field in autocomplete_data
        if not (field_value := field["value"]).endswith(".type")
    ]

    if not prefix:
        # Returns first 20 fields if no prefix is provided
        return fields[:20]
    return fields


def cli_search(args: argparse.Namespace):
    """Search subcommand.

    Args:
        args (Namespace): Argparse Namespace.

    Raises:
        CensysCLIException: If invalid options are provided.
    """
    index_type = args.index_type or args.query_type

    if args.open:
        url_query = {"q": args.query, "resource": index_type}
        webbrowser.open(
            f"https://search.censys.io/search?{urlencode(url_query)}"  # noqa: E231
        )
        sys.exit(0)

    if args.timeout < 1:
        raise CensysCLIException("Timeout must be greater than 0.")

    censys_args = {
        "timeout": args.timeout,
    }

    if args.api_id:
        censys_args["api_id"] = args.api_id

    if args.api_secret:
        censys_args["api_secret"] = args.api_secret

    c = SearchClient(**censys_args)

    search_args = {}
    write_args = {"file_format": args.format, "file_path": args.output}
    results: List[Dict[str, Any]] = []

    index: CensysSearchAPIv2 = getattr(c.v2, index_type)

    search_args.update(
        {
            "pages": args.pages,
            "per_page": args.per_page,
            "fields": args.fields,
        }
    )
    if index_type == "hosts":
        search_args.update(
            {
                "sort": args.sort_order,
                "virtual_hosts": args.virtual_hosts,
            }
        )
    elif index_type == "certificates":
        search_args.update({"sort": args.sort})

    if args.output and not args.output.endswith(".json"):
        raise CensysCLIException(
            "JSON is the only valid file format for Search 2.0 responses."
        )
    write_args.update(
        {
            "file_format": "json" if args.output else "screen",
        }
    )

    with err_console.status("Searching"):
        try:
            for page in index.search(args.query, **search_args):
                results.extend(page)
        except Exception:
            err_console.print_exception(max_frames=4)
        except KeyboardInterrupt:  # pragma: no cover
            pass

    try:
        write_file(results, **write_args)
    except ValueError as error:  # pragma: no cover
        err_console.print(f"Error writing log file. Error: {error}")


def include(parent_parser: argparse._SubParsersAction, parents: dict):
    """Include this subcommand into the parent parser.

    Args:
        parent_parser (argparse._SubParsersAction): Parent parser.
        parents (dict): Parent arg parsers.
    """
    search_parser = parent_parser.add_parser(
        "search",
        description="Query Censys Search for resource data by providing a query \
            string, the resource index, and the fields to be returned",
        help="query Censys search",
        parents=[parents["auth"]],
    )
    search_parser.add_argument(
        "query",
        type=str,
        help="a string written in Censys Search syntax",
    ).completer = fields_completer

    index_metavar = "|".join(V2_INDEXES)
    index_default = "hosts"
    search_parser.add_argument(
        "--index-type",
        type=str,
        default=index_default,
        choices=V2_INDEXES,
        metavar=index_metavar,
        help="which resource index to query",
    )
    # Backwards compatibility
    search_parser.add_argument(
        "-f",
        "--format",
        type=str,
        default="screen",
        choices=["screen", "json"],
        metavar="screen|json",
        help=argparse.SUPPRESS,
    )
    search_parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="output file path",
    )
    search_parser.add_argument(
        "-O",
        "--open",
        action="store_true",
        help="open query in browser",
    )

    search_parser.add_argument(
        "--pages",
        default=1,
        type=int,
        help="number of pages of results to return (when set to -1 returns all pages available)",
    )
    search_parser.add_argument(
        "--per-page",
        default=100,
        type=int,
        help="number of results to return per page",
    )
    search_parser.add_argument(
        "--timeout",
        default=30,
        type=int,
        help="number of seconds to wait for a response",
    )
    search_parser.add_argument(
        "--fields",
        dest="fields",
        type=str,
        nargs="+",
        help="additional fields to return in the matching results",
    ).completer = fields_completer

    hosts_group = search_parser.add_argument_group("hosts specific arguments")
    hosts_group.add_argument(
        "--sort-order",
        dest="sort_order",
        type=str,
        default="RELEVANCE",
        choices=["RELEVANCE", "ASCENDING", "DESCENDING", "RANDOM"],
        help="sort order of results",
    )
    hosts_group.add_argument(
        "--virtual-hosts",
        type=str,
        default="EXCLUDE",
        choices=["INCLUDE", "EXCLUDE", "ONLY"],
        metavar="INCLUDE|EXCLUDE|ONLY",
        help="whether to include virtual hosts in the results",
    )

    certs_group = search_parser.add_argument_group("certificates specific arguments")
    certs_group.add_argument(
        "--sort",
        dest="sort",
        type=str,
        nargs="+",
        help="fields to sort by",
    )

    search_parser.set_defaults(func=cli_search)
