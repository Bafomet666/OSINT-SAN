"""Censys view CLI."""

import argparse
import ipaddress
import sys
import webbrowser

from censys.cli.utils import (
    V2_INDEXES,
    console,
    err_console,
    valid_datetime_type,
    write_file,
)
from censys.common.exceptions import CensysCLIException
from censys.search import SearchClient
from censys.search.v2.api import CensysSearchAPIv2


def cli_view(args: argparse.Namespace):
    """Search subcommand.

    Args:
        args (Namespace): Argparse Namespace.

    Raises:
        CensysCLIException: If invalid options are provided.
    """
    if args.open:
        webbrowser.open(
            f"https://search.censys.io/{args.index_type}/{args.document_id}"  # noqa: E231
        )
        sys.exit(0)

    censys_args = {}

    if args.api_id:
        censys_args["api_id"] = args.api_id

    if args.api_secret:
        censys_args["api_secret"] = args.api_secret

    c = SearchClient(**censys_args)

    index_type = args.index_type

    if index_type == "hosts":
        try:
            ip_address = args.document_id
            if "+" in ip_address:
                ip_address, _ = args.document_id.split("+")
            ipaddress.ip_address(ip_address)
        except ValueError:
            if len(args.document_id) == 64:
                err_console.print(
                    "This is a SHA-256 certificate fingerprint. Switching to certificates index."
                )
                index_type = "certificates"
            else:
                raise CensysCLIException(
                    f"Invalid IP address: {args.document_id}. Please provide a valid IPv4 or IPv6 address."
                )

    index: CensysSearchAPIv2 = getattr(c.v2, index_type)

    view_args = {}
    write_args = {
        "file_format": "json" if args.output else "screen",
        "file_path": args.output,
    }

    if args.at_time:
        if index_type == "hosts":
            view_args["at_time"] = args.at_time
        else:
            err_console.print(
                "The --at-time option is only supported for the hosts index. Ignoring."
            )

    document = index.view(args.document_id, **view_args)

    try:
        write_file(document, **write_args)
    except ValueError as error:  # pragma: no cover
        console.print(f"Error writing log file. Error: {error}")


def include(parent_parser: argparse._SubParsersAction, parents: dict):
    """Include this subcommand into the parent parser.

    Args:
        parent_parser (argparse._SubParsersAction): Parent parser.
        parents (dict): Parent arg parsers.
    """
    view_parser = parent_parser.add_parser(
        "view",
        description="View a document in Censys Search by providing a document \
            id and the resource index",
        help="view document",
        parents=[parents["auth"]],
    )
    view_parser.add_argument(
        "document_id",
        type=str,
        help="a document id (IP address or SHA-256 certificate fingerprint) to view",
    )
    view_parser.add_argument(
        "--index-type",
        type=str,
        default="hosts",
        choices=V2_INDEXES,
        metavar="|".join(V2_INDEXES),
        help="which resource index to query",
    )
    view_parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="json output file path",
    )
    view_parser.add_argument(
        "-O",
        "--open",
        action="store_true",
        help="open document in browser",
    )

    hosts_group = view_parser.add_argument_group("hosts specific arguments")
    hosts_group.add_argument(
        "--at-time",
        type=valid_datetime_type,
        metavar="YYYY-MM-DD (HH:mm)",
        help="Fetches a document at a given point in time",
    )

    view_parser.set_defaults(func=cli_view)
