"""Interact with the Censys Saved Queries API."""

from typing import Optional

from .api import CensysAsmAPI


class SavedQueries(CensysAsmAPI):
    """Saved Queries API class."""

    base_path = "/inventory/v1/saved-query"

    def get_saved_queries(
        self,
        query_name_prefix: Optional[str] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        filter_term: Optional[str] = None,
    ) -> dict:
        """Get saved queries.

        Args:
            query_name_prefix (str, optional): Prefix for the saved query name.
            page_size (int, optional): Number of results to return. Defaults to 50.
            page (int, optional): Page number to begin at when searching. Defaults to 1.
            filter_term (str, optional): Term used to filter the list of saved query names and the saved queries.

        Returns:
            dict: Saved queries results.
        """
        if page_size is None:
            page_size = 50
        if page is None:
            page = 1
        args: dict = {
            "pageSize": page_size,
            "page": page,
        }

        if query_name_prefix:
            args["queryNamePrefix"] = query_name_prefix
        if filter_term:
            args["filterTerm"] = filter_term

        return self._get(self.base_path, args=args)

    def add_saved_query(
        self,
        query: str,
        query_name: str,
    ) -> dict:
        """Add a new saved query to the ASM platform.

        Args:
            query (str): Query string.
            query_name (str): Saved query name.

        Returns:
            dict: Added saved query results.
        """
        body = {
            "query": query,
            "queryName": query_name,
        }

        return self._post(self.base_path, data=body)

    def get_saved_query_by_id(
        self,
        query_id: str,
    ) -> dict:
        """Get saved query by query ID.

        Args:
            query_id (str): The saved query's ID.

        Returns:
            dict: Saved query result.
        """
        return self._get(f"{self.base_path}/{query_id}")

    def edit_saved_query_by_id(
        self,
        query_id: str,
        query: str,
        query_name: str,
    ) -> dict:
        """Edit an existing saved query by query ID.

        Args:
            query_id (str): The saved query's ID.
            query (str): New query string.
            query_name (str): New saved query name.

        Returns:
            dict: Edited saved query result.
        """
        body = {
            "query": query,
            "queryName": query_name,
        }

        return self._put(f"{self.base_path}/{query_id}", data=body)

    def delete_saved_query_by_id(
        self,
        query_id: str,
    ) -> dict:
        """Delete saved query by query ID.

        Args:
            query_id (str): The saved query's ID.

        Returns:
            dict: Delete results.
        """
        return self._delete(f"{self.base_path}/{query_id}")
