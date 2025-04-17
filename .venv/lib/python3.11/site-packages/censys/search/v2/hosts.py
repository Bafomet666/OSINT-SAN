"""Interact with the Censys Search Host API."""

from typing import Any, Dict, List, Optional, Union

from .api import CensysSearchAPIv2
from censys.common.types import Datetime
from censys.common.utils import format_rfc3339


class CensysHosts(CensysSearchAPIv2):
    """Interacts with the Hosts index.

    Examples:
        Inits Censys Hosts.

        >>> from censys.search import CensysHosts
        >>> h = CensysHosts()

        Simple host search.

        >>> for page in h.search("services.service_name: HTTP"):
        >>>     print(page)
        [
            {
            'services':
                [
                    {'service_name': 'HTTP', 'port': 80},
                    {'service_name': 'HTTP', 'port': 443}
                ],
            'ip': '1.0.0.0'
            },
            ...
        ]

        Fetch a specific host and its services

        >>> h.view("1.0.0.0")
        {
            'ip': '8.8.8.8',
            'services': [{}],
            ...
        }

        Simple host aggregate.

        >>> h.aggregate("services.service_name: HTTP", "services.port", num_buckets=5)
        {
            'total_omitted': 591527370,
            'buckets': [
                {'count': 56104072, 'key': '80'},
                {'count': 43527894, 'key': '443'},
                {'count': 23070429, 'key': '7547'},
                {'count': 12970769, 'key': '30005'},
                {'count': 12825150, 'key': '22'}
            ],
            'potential_deviation': 3985101,
            'field': 'services.port',
            'query': 'services.service_name: HTTP',
            'total': 172588754
        }

        Fetch a list of host names for the specified IP address.

        >>> h.view_host_names("1.1.1.1")
        ['one.one.one.one']

        Fetch a list of events for the specified IP address.

        >>> h.view_host_events("1.1.1.1")
        [{'timestamp': '2019-01-01T00:00:00.000Z'}]
    """

    INDEX_NAME = "hosts"
    """Name of Censys Index."""

    def __init__(
        self, api_id: Optional[str] = None, api_secret: Optional[str] = None, **kwargs
    ):
        """Inits CensysHosts.

        See CensysSearchAPIv2 for additional arguments.

        Args:
            api_id (Optional[str], optional): API ID. Defaults to None.
            api_secret (Optional[str], optional): API Secret. Defaults to None.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(api_id=api_id, api_secret=api_secret, **kwargs)
        self.metadata_path = f"/v2/metadata/{self.INDEX_NAME}"

    def view(
        self,
        document_id: str,
        at_time: Optional[Datetime] = None,
        **kwargs: Any,
    ) -> dict:
        """View document from current index.

        View the current structured data we have on a specific document.
        For more details, see our documentation: https://search.censys.io/api

        Args:
            document_id (str): The ID of the document you are requesting.
            at_time ([str, datetime.date, datetime.datetime]):
                Optional; Fetches a document at a given point in time.
            **kwargs (Any): Optional; Additional arguments to be passed to the query.

        Returns:
            dict: The result set returned.
        """
        args = {}
        if at_time:
            args["at_time"] = format_rfc3339(at_time)

        return super().view(document_id, **args)

    def bulk_view(
        self,
        document_ids: List[str],
        max_workers: int = 20,
        at_time: Optional[Datetime] = None,
        **kwargs: Any,
    ) -> Dict[str, dict]:
        """Bulk view documents from current index.

        View the current structured data we have on a list of documents.

        Args:
            document_ids (List[str]): The IDs of the documents you are requesting.
            max_workers (int): Optional; The number of workers to use. Defaults to 20.
            at_time ([str, datetime.date, datetime.datetime]):
                Optional; Fetches a document at a given point in time.
            **kwargs (Any): Optional; Additional arguments to be passed to the query.

        Returns:
            Dict[str, dict]: The result set returned.
        """
        if at_time:
            kwargs["at_time"] = format_rfc3339(at_time)
        return super().bulk_view(document_ids, max_workers, **kwargs)

    def search(
        self,
        query: str,
        per_page: int = 100,
        cursor: Optional[str] = None,
        pages: int = 1,
        fields: Optional[List[str]] = None,
        sort: Optional[Union[str, List[str]]] = None,
        virtual_hosts: Optional[str] = None,
        **kwargs: Any,
    ) -> CensysSearchAPIv2.Query:
        """Search host index.

        Searches the given index for all records that match the given query.
        For more details, see our documentation: https://search.censys.io/api

        Args:
            query (str): The query to be executed.
            per_page (int): Optional; The number of results to be returned for each page. Defaults to 100.
            cursor (int): Optional; The cursor of the desired result set.
            pages (int): Optional; The number of pages returned. Defaults to 1.
            fields (List[str]): Optional; The fields to return. Defaults to all fields.
            sort (str): Optional; The method used to sort results. Valid values are "RELEVANCE", "DESCENDING", and "ASCENDING".
            virtual_hosts (str): Optional; Whether to include virtual hosts in the results. Valid values are "EXCLUDE", "INCLUDE", and "ONLY".
            **kwargs (Any): Optional; Additional arguments to be passed to the query.

        Returns:
            Query: Query object that can be a callable or an iterable.
        """
        if virtual_hosts:
            kwargs["virtual_hosts"] = virtual_hosts
        return super().search(query, per_page, cursor, pages, fields, sort, **kwargs)

    def aggregate(
        self,
        query: str,
        field: str,
        num_buckets: int = 50,
        virtual_hosts: Optional[str] = None,
        **kwargs: Any,
    ) -> dict:
        """Aggregate host index.

        Creates a report on the breakdown of the values of a field in a result set.
        For more details, see our documentation: https://search.censys.io/api

        Args:
            query (str): The query to be executed.
            field (str): The field you are running a breakdown on.
            num_buckets (int): Optional; The maximum number of values. Defaults to 50.
            virtual_hosts (str): Optional; Whether to include virtual hosts in the results. Valid values are "EXCLUDE", "INCLUDE", and "ONLY".
            **kwargs (Any): Optional; Additional arguments to be passed to the query.

        Returns:
            dict: The result set returned.
        """
        if virtual_hosts:
            kwargs["virtual_hosts"] = virtual_hosts
        return super().aggregate(query, field, num_buckets, **kwargs)

    def metadata(self) -> dict:
        """Get metadata for the host index.

        Returns:
            dict: The result set returned.
        """
        return self._get(self.metadata_path)["result"]

    def view_host_names(
        self, ip: str, per_page: Optional[int] = None, cursor: Optional[str] = None
    ) -> List[str]:
        """Fetches a list of host names for the specified IP address.

        Args:
            ip (str): The IP address of the requested host.
            per_page (int): Optional; The number of results to be returned for each page. Defaults to 100.
            cursor (int): Optional; The cursor of the desired result set.

        Returns:
            List[str]: A list of host names.
        """
        args = {"per_page": per_page, "cursor": cursor}
        return self._get(self.view_path + ip + "/names", args)["result"]["names"]

    def view_host_diff(
        self,
        ip: str,
        ip_b: Optional[str] = None,
        at_time: Optional[Datetime] = None,
        at_time_b: Optional[Datetime] = None,
    ):
        """Fetches a diff of the specified IP address.

        Args:
            ip (str): The IP address of the requested host.
            ip_b (str): Optional; The IP address of the second host.
            at_time (Datetime): Optional; An RFC3339 timestamp which represents
                the point-in-time used as the basis for Host A.
            at_time_b (Datetime): Optional; An RFC3339 timestamp which represents
                the point-in-time used as the basis for Host B.

        Returns:
            dict: A diff of the hosts.
        """
        args: Dict[str, Any] = {}
        if ip_b:
            args["ip_b"] = ip_b
        if at_time:
            args["at_time"] = format_rfc3339(at_time)
        if at_time_b:
            args["at_time_b"] = format_rfc3339(at_time_b)
        return self._get(self.view_path + ip + "/diff", args)["result"]

    def view_host_events(
        self,
        ip: str,
        start_time: Optional[Datetime] = None,
        end_time: Optional[Datetime] = None,
        per_page: Optional[int] = None,
        cursor: Optional[str] = None,
        reversed: Optional[bool] = None,
    ) -> dict:
        """Fetches a list of events for the specified IP address.

        Args:
            ip (str): The IP address of the requested host.
            start_time (Datetime): Optional; An RFC3339 timestamp which represents
                the beginning chronological point-in-time (inclusive) from which events are returned.
            end_time (Datetime): Optional; An RFC3339 timestamp which represents
                the ending chronological point-in-time (exclusive) from which events are returned.
            per_page (int): Optional; The maximum number of hits to return in each response
                (minimum of 1, maximum of 50).
            cursor (str): Optional; Cursor token from the API response.
            reversed (bool): Optional; Reverse the order of the return events,
                that is, return events in reversed chronological order.

        Returns:
            dict: A list of events.
        """
        args = {"per_page": per_page, "cursor": cursor, "reversed": reversed}
        if start_time:
            args["start_time"] = format_rfc3339(start_time)
        if end_time:
            args["end_time"] = format_rfc3339(end_time)

        return self._get(f"/v2/experimental/{self.INDEX_NAME}/{ip}/events", args)[
            "result"
        ]

    def view_host_certificates(
        self,
        ip: str,
        per_page: int = 100,
        start_time: Optional[Datetime] = None,
        cursor: Optional[str] = None,
    ) -> dict:
        """Returns a list of certificates for the specified host.

        Args:
            ip (str): The IP address of the requested host.
            per_page (int): Optional; The number of results to be returned for each page. Defaults to 100.
            start_time (Datetime): Optional; An RFC3339 timestamp which represents
                the beginning chronological point-in-time (inclusive) from which events are returned.
            cursor (str): Optional; Cursor token from the API response.

        Returns:
            dict: A list of certificates.
        """
        args = {"per_page": per_page, "cursor": cursor}
        if start_time:
            args["start_time"] = format_rfc3339(start_time)
        return self._get(f"/v2/{self.INDEX_NAME}/{ip}/certificates", args)["result"]

    def list_hosts_with_tag(self, tag_id: str) -> List[str]:
        """Returns a list of hosts which are tagged with the specified tag.

        Args:
            tag_id (str): The ID of the tag.

        Returns:
            List[str]: A list of host IP addresses.
        """
        hosts = self._list_documents_with_tag(tag_id, "hosts", "hosts")
        return [host["ip"] for host in hosts]
