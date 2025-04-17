"""Interact with the Censys Search Cert API."""

import warnings
from typing import List, Optional, Union

from ...common.types import Datetime
from ...common.utils import format_rfc3339
from .api import CensysSearchAPIv2


class CensysCerts(CensysSearchAPIv2):
    """Interacts with the Certs index.

    Please note that this class represents only the v2 API endpoints.

    Examples:
        Inits Censys Certs.

        >>> from censys.search import CensysCerts
        >>> c = CensysCerts()

        Search for hosts by sha256fp.

        >>> c.get_hosts_by_cert("fb444eb8e68437bae06232b9f5091bccff62a768ca09e92eb5c9c2cf9d17c426")
        (
            [
                {
                    "ip": "string",
                    "name": "string",
                    "observed_at": "2021-08-02T14:56:38.711Z",
                    "first_observed_at": "2021-08-02T14:56:38.711Z",
                }
            ],
            {
                "next": "nextCursorToken",
            },
        )
    """

    INDEX_NAME = "certificates"
    """Name of Censys Index."""

    def __init__(
        self, api_id: Optional[str] = None, api_secret: Optional[str] = None, **kwargs
    ):
        """Inits CensysCerts.

        See CensysSearchAPIv2 for additional arguments.

        Args:
            api_id (Optional[str], optional): API ID. Defaults to None.
            api_secret (Optional[str], optional): API Secret. Defaults to None.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(api_id=api_id, api_secret=api_secret, **kwargs)
        self.bulk_path = f"/v2/{self.INDEX_NAME}/bulk"

    def view(self, document_id: str, **kwargs) -> dict:
        """Fetches the certificate record for the specified SHA-256 fingerprint.

        Args:
            document_id (str): The SHA-256 fingerprint of the requested certificate.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: Certificate details.
        """
        return self._get(self.view_path + document_id, args=kwargs)["result"]

    def bulk_post(self, fingerprints: List[str]) -> List[dict]:
        """Fetches the certificate records for the specified SHA-256 fingerprints.

        Using the POST method allows for a larger number of fingerprints to be queried at once.

        Args:
            fingerprints (List[str]): List of certificate SHA256 fingerprints.

        Returns:
            dict: Certificate details.
        """
        data = {"fingerprints": fingerprints}
        return self._post(self.bulk_path, data=data)["result"]

    def bulk_get(self, fingerprints: List[str]) -> List[dict]:
        """Fetches the certificate records for the specified SHA-256 fingerprints.

        Using the GET method allows for a smaller number of fingerprints to be queried at once.

        Args:
            fingerprints (List[str]): List of certificate SHA256 fingerprints.

        Returns:
            dict: Certificate details.
        """
        args = {"fingerprints": fingerprints}
        return self._get(self.bulk_path, args=args)["result"]

    def bulk(self, fingerprints: List[str]) -> List[dict]:
        """Fetches the certificate records for the specified SHA-256 fingerprints.

        By default, this function uses the POST method, which allows for a larger number of fingerprints to be queried at once.
        If you wish to use the GET method, please use `CensysCerts.bulk_get` instead.

        Args:
            fingerprints (List[str]): List of certificate SHA256 fingerprints.

        Returns:
            dict: Certificate details.
        """
        return self.bulk_post(fingerprints)

    def bulk_view(self, fingerprints: List[str]) -> List[dict]:  # type: ignore[override]
        """Fetches the certificate records for the specified SHA-256 fingerprints.

        By default, this function uses the POST method, which allows for a larger number of fingerprints to be queried at once.
        If you wish to use the GET method, please use `CensysCerts.bulk_get` instead.

        Args:
            fingerprints (List[str]): List of certificate SHA256 fingerprints.

        Returns:
            dict: Certificate details.
        """
        return self.bulk_post(fingerprints)

    def search_post_raw(
        self,
        query: str,
        per_page: int = 50,
        cursor: Optional[str] = None,
        fields: Optional[List[str]] = None,
        sort: Optional[Union[str, List[str]]] = None,
        **kwargs,
    ) -> dict:
        """Searches the Certs index using the POST method. Returns the raw response.

        Args:
            query (str): The query string to search for.
            per_page (int): The number of results to return per page. Defaults to 50.
            cursor (str, optional): Cursor token from the API response, which fetches the next page of results when added to the endpoint URL.
            fields (List[str], optional): Additional fields to return in the matched certificates outside of the default returned fields.
            sort (List[str], optional): A list of fields to sort on. By default, fields will be sorted in ascending order.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: Search results.
        """
        return super().search_post_raw(
            query=query,
            per_page=per_page,
            cursor=cursor,
            fields=fields,
            sort=sort,
            **kwargs,
        )

    def search_post(
        self,
        query: str,
        per_page: int = 50,
        cursor: Optional[str] = None,
        fields: Optional[List[str]] = None,
        sort: Optional[Union[str, List[str]]] = None,
        **kwargs,
    ) -> dict:
        """Searches the Certs index using the POST method.

        This method returns the `result` field of the raw response.
        If you wish to access the raw response, please use `CensysCerts.search_post_raw` instead.

        Args:
            query (str): The query string to search for.
            per_page (int): The number of results to return per page. Defaults to 50.
            cursor (str, optional): Cursor token from the API response, which fetches the next page of results when added to the endpoint URL.
            fields (List[str], optional): Additional fields to return in the matched certificates outside of the default returned fields.
            sort (List[str], optional): A list of fields to sort on. By default, fields will be sorted in ascending order.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: Search results.
        """
        return super().search_post(
            query=query,
            per_page=per_page,
            cursor=cursor,
            fields=fields,
            sort=sort,
            **kwargs,
        )

    def search_get(
        self,
        query: str,
        per_page: int = 50,
        cursor: Optional[str] = None,
        fields: Optional[List[str]] = None,
        sort: Optional[Union[str, List[str]]] = None,
        **kwargs,
    ) -> dict:
        """Searches the Certs index using the GET method.

        Args:
            query (str): The query string to search for.
            per_page (int): The number of results to return per page. Defaults to 50.
            cursor (str, optional): Cursor token from the API response, which fetches the next page of results when added to the endpoint URL.
            fields (List[str], optional): Additional fields to return in the matched certificates outside of the default returned fields.
            sort (List[str], optional): A list of fields to sort on. By default, fields will be sorted in ascending order.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: Search results.
        """
        return super().search_get(
            query=query,
            per_page=per_page,
            cursor=cursor,
            fields=fields,
            sort=sort,
            **kwargs,
        )

    def raw_search(
        self,
        query: str,
        per_page: int = 50,
        cursor: Optional[str] = None,
        fields: Optional[List[str]] = None,
        sort: Optional[Union[str, List[str]]] = None,
        **kwargs,
    ) -> dict:
        """Searches the Certs index.

        Searches the Certs index for all records that match the given query.
        This method does no automatic pagination or post processing.

        Args:
            query (str): The query string to search for.
            per_page (int): The number of results to return per page. Defaults to 50.
            cursor (str, optional): Cursor token from the API response, which fetches the next page of results when added to the endpoint URL.
            fields (List[str], optional): Additional fields to return in the matched certificates outside of the default returned fields.
            sort (List[str], optional): A list of fields to sort on. By default, fields will be sorted in ascending order.
            **kwargs: Additional keyword arguments to pass to the underlying HTTP request.

        Returns:
            dict: Search results.
        """
        return super().raw_search(
            query=query,
            per_page=per_page,
            cursor=cursor,
            fields=fields,
            sort=sort,
            **kwargs,
        )

    def search(  # type: ignore[override]
        self,
        query: str,
        per_page: int = 50,
        cursor: Optional[str] = None,
        pages: int = 1,
        fields: Optional[List[str]] = None,
        sort: Optional[Union[str, List[str]]] = None,
        **kwargs,
    ) -> CensysSearchAPIv2.Query:
        """Searches the Certs index.

        By default, this function uses the POST method, which allows for a larger number of fingerprints to be queried at once.
        If you wish to use the GET method, please use `CensysCerts.search_get` instead.

        Args:
            query (str): The query string to search for.
            per_page (int): The number of results to return per page. Defaults to 50.
            cursor (str, optional): Cursor token from the API response, which fetches the next page of results when added to the endpoint URL.
            pages (int): The number of pages to return. Defaults to 1.
            fields (List[str], optional): Additional fields to return in the matched certificates outside of the default returned fields.
            sort (List[str], optional): A list of fields to sort on. By default, fields will be sorted in ascending order.
            **kwargs: Additional keyword arguments to pass to the underlying HTTP request.

        Returns:
            Query: A query object that can be used to iterate over the search results.
        """
        return super().search(query, per_page, cursor, pages, fields, sort, **kwargs)

    def aggregate(
        self, query: str, field: str, num_buckets: int = 50, **kwargs
    ) -> dict:
        """Aggregates certificate records matching a specified query into buckets based on the given field.

        Args:
            query (str): The query string to search for.
            field (str): The field to aggregate on.
            num_buckets (int): The number of buckets to return. Defaults to 50.
            **kwargs: Additional keyword arguments to pass to the underlying HTTP request.

        Returns:
            dict: Aggregation results.
        """
        args = {"q": query, "field": field, "num_buckets": num_buckets}
        args.update(kwargs)
        return self._get(self.aggregate_path, args=args)["result"]

    def get_hosts_by_cert(self, fingerprint: str, cursor: Optional[str] = None) -> dict:
        """Returns a list of hosts which contain services presenting this certificate, including when the certificate was first observed.

        Args:
            fingerprint (str): The SHA-256 fingerprint of the requested certificate.
            cursor (str): Cursor token from the API response, which fetches the next page of hosts when added to the endpoint URL.

        Returns:
            dict: A list of hosts which contain services presenting this certificate.
        """
        warnings.warn(
            "This API endpoint is deprecated and scheduled for removal during a future release. Users should migrate to using the search endpoint on the Host index using the 'services.certificate: {fingerprint}' query to find any hosts currently presenting a certificate.",
            category=DeprecationWarning,
            stacklevel=2,
        )
        args = {"cursor": cursor}
        return self._get(self.view_path + fingerprint + "/hosts", args)["result"]

    def list_certs_with_tag(self, tag_id: str) -> List[dict]:
        """Returns a list of certs which are tagged with the specified tag.

        Args:
            tag_id (str): The ID of the tag.

        Returns:
            List[dict]: A list of certs which are tagged with the specified tag.
        """
        return self._list_documents_with_tag(tag_id, "certificates", "certs")

    def get_observations(
        self,
        fingerprint: str,
        per_page: int = 50,
        start_time: Optional[Datetime] = None,
        end_time: Optional[Datetime] = None,
        cursor: Optional[str] = None,
    ) -> dict:
        """Returns a list of observations for the specified certificate.

        Args:
            fingerprint (str): The SHA-256 fingerprint of the requested certificate.
            per_page (int): The number of results to return per page. Defaults to 50.
            start_time (str): The start time of the observations to return.
            end_time (str): The end time of the observations to return.
            cursor (str): Cursor token from the API response, which fetches the next page of observations when added to the endpoint URL.

        Returns:
            dict: A list of observations for the specified certificate.
        """
        args = {"per_page": per_page, "cursor": cursor}
        if start_time:
            args["start_time"] = format_rfc3339(start_time)
        if end_time:
            args["end_time"] = format_rfc3339(end_time)
        return self._get(self.view_path + fingerprint + "/observations", args)["result"]
