"""Interact with the Censys Web Entities Assets API."""

from typing import Iterator, Optional

from .assets import Assets


class WebEntitiesAssets(Assets):
    """Web Entities Assets API class."""

    def __init__(self, *args, **kwargs):
        """Inits WebEntitiesAssets.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__("web-entities", *args, **kwargs)

    def get_assets(self, *args, **kwargs):
        """Requests assets data.

        This method is not implemented for web entities.
        Please see the inventory search and aggregation API.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Raises:
            NotImplementedError: This method is not implemented.
        """
        raise NotImplementedError("This method is not implemented.")

    def get_instances(
        self,
        name_and_port: str,
        page_size: Optional[int] = None,
        cursor: Optional[str] = None,
    ) -> Iterator[dict]:
        """List all instances of the web entity.

        Args:
            name_and_port: (str): Web entity to query.
            page_size (int): Optional; Page size for retrieving assets.
            cursor (str): Optional; Cursor to use for pagination.

        Yields:
            dict: The assets result returned.
        """
        args = {"pageSize": page_size, "cursor": cursor}

        while True:
            res = self._get(f"{self.base_path}/{name_and_port}/instances", args=args)
            yield from res.get("instances", [])
            cursor = res.get("cursor")
            if not cursor:
                break
            args["cursor"] = cursor
