"""Interact with miscellaneous Censys Beta APIs."""

from typing import List, Optional

from ..common.types import Datetime
from ..common.utils import format_iso8601
from .api import CensysAsmAPI


class Beta(CensysAsmAPI):
    """Beta API class."""

    base_path = "/beta"

    def get_logbook_data(
        self, filters: Optional[dict] = None, cursor: Optional[str] = None
    ):
        """Retrieve logbook data.

        Args:
            filters (dict): Optional; Filter parameters.
            cursor (str): Optional; Cursor for pagination.

        Returns:
            dict: Logbook data result.
        """
        data = {"filters": filters, "nextWindowCursor": cursor}
        return self._post(f"{self.base_path}/logbook/getLogbookData", data=data)

    def add_cloud_assets(
        self,
        cloud_connector_uid: str,
        cloud_assets: List[dict],
    ):
        """Add cloud assets.

        Args:
            cloud_connector_uid (str): Cloud connector UID.
            cloud_assets (List[dict]): Cloud assets.

        Returns:
            dict: Add cloud assets result.
        """
        data = {
            "cloudConnectorUid": cloud_connector_uid,
            "cloudAssets": cloud_assets,
        }
        return self._post(f"{self.base_path}/cloudConnector/addCloudAssets", data=data)

    def get_input_assets(self, page_number: int = 1, page_size: Optional[int] = None):
        """Retrieve input assets.

        Args:
            page_number (int): Optional; Page number to begin at when searching.
            page_size (int): Optional; Page size for retrieving assets.

        Returns:
            dict: Input assets result.
        """
        return self._get(
            f"{self.base_path}/assets/inputAssets",
            params={"pageNumber": page_number, "pageSize": page_size},
        )

    def get_asset_counts(self, since: Datetime, environment: str, asset_type: str):
        """Retrieve asset counts.

        Args:
            since (Datetime): Date to include assets from.
            environment (str): Environment to include assets from.
            asset_type (str): Asset type to include.

        Returns:
            dict: Asset count result.
        """
        params = {
            "since": format_iso8601(since),
            "environment": environment,
            "assetType": asset_type,
        }
        return self._get(
            f"{self.base_path}/assets/counts",
            params=params,
        )

    def get_host_counts_by_country(self, since: Datetime, environment: str):
        """Retrieve host counts by country.

        Args:
            since (Datetime): Date to include hosts from.
            environment (str): Environment to include hosts from.

        Returns:
            dict: Host count result.
        """
        params = {
            "since": format_iso8601(since),
            "environment": environment,
        }
        return self._get(
            f"{self.base_path}/assets/hostCountsByCountry",
            params=params,
        )

    def get_user_workspaces(self, user_uuid: str):
        """Retrieve user workspaces.

        Args:
            user_uuid (str): User UUID.

        Returns:
            dict: User workspaces result.
        """
        return self._get(
            f"{self.base_path}/users/{user_uuid}/workspaces",
        )
