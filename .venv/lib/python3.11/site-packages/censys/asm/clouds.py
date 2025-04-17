"""Interact with the Censys Clouds API."""

from ..common.types import Datetime
from ..common.utils import format_iso8601
from .api import CensysAsmAPI


class Clouds(CensysAsmAPI):
    """Clouds API class."""

    base_path = "/v1/clouds"

    def get_host_counts(
        self,
        since: Datetime,
    ) -> dict:
        """Retrieve host counts by cloud.

        Hosts found after the date provided in the `since` parameter will be included in the new asset counts.

        Args:
            since (Datetime): Date to include hosts from.

        Returns:
            dict: Host count result.
        """
        since = format_iso8601(since)
        return self._get(f"{self.base_path}/hostCounts/{since}")

    def get_domain_counts(self, since: Datetime) -> dict:
        """Retrieve domain counts by cloud.

        Args:
            since (Datetime): Date to include domains from.

        Returns:
            dict: Domain count result.
        """
        since = format_iso8601(since)
        return self._get(f"{self.base_path}/domainCounts/{since}")

    def get_object_store_counts(self, since: Datetime) -> dict:
        """Retrieve object store counts by cloud.

        Args:
            since (Datetime): Date to include object stores from.

        Returns:
            dict: Object store count result.
        """
        since = format_iso8601(since)
        return self._get(f"{self.base_path}/objectStoreCounts/{since}")

    def get_subdomain_counts(self, since: Datetime) -> dict:
        """Retrieve subdomain counts by cloud.

        Args:
            since (Datetime): Date to include subdomains from.

        Returns:
            dict: Subdomain count result.
        """
        since = format_iso8601(since)
        return self._get(f"{self.base_path}/subdomainCounts/{since}")

    def get_unknown_counts(self) -> dict:
        """Retrieve known and unknown counts for hosts by cloud.

        Returns:
            dict: Unknown count result.
        """
        return self._get(f"{self.base_path}/unknownCounts")
