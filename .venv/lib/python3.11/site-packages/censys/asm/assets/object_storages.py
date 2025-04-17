"""Interact with the Censys Object Storage Assets API."""

from urllib.parse import quote

from .assets import Assets


class ObjectStoragesAssets(Assets):
    """Object Storage Assets API class.

    Please note that the Object Storage Assets API is currently in beta and
    is subject to change.
    """

    def __init__(self, *args, **kwargs):
        """Inits ObjectStoragesAssets.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__("object-storages", api_version="beta", *args, **kwargs)

    def _format_asset_id(self, asset_id: str) -> str:
        """Formats asset ID.

        Args:
            asset_id (str): Asset ID to format.

        Returns:
            str: Formatted asset ID.
        """
        return quote(asset_id, safe="")
