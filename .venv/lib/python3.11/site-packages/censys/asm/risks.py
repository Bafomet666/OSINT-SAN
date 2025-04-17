"""Interact with the Censys Risks API."""

import urllib.parse
from typing import Any, Dict, List, Optional

from .api import CensysAsmAPI


class Risks(CensysAsmAPI):
    """Risks API class."""

    base_path = "/v2/risk"
    risk_events_path = f"{base_path}-events"
    risk_instances_path = f"{base_path}-instances"
    risk_types_path = f"{base_path}-types"

    def get_risk_events(
        self,
        start: Optional[str] = None,
        end: Optional[str] = None,
        after_id: Optional[int] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        accept: Optional[str] = None,
    ) -> dict:
        """Retrieve risk events.

        Args:
            start (str): Optional; Starting event time, inclusive (in RFC3339 format).
            end (str): Optional; Ending event time, inclusive (in RFC3339 format).
            after_id (int): Optional; Risk event ID to query for events after.
            limit (int): Optional; Max number of events to return.
            cursor (str): Optional; Cursor value to continue collecting events started in a previous request.
            accept (str): Optional; Accept header.

        Returns:
            dict: Risk events result.
        """
        args: Dict[str, Any] = {}
        if start:
            args["start"] = start
        if end:
            args["end"] = end
        if after_id:
            args["afterID"] = after_id
        if limit:
            args["limit"] = limit
        if cursor:
            args["cursor"] = cursor
        return self._get(
            self.risk_events_path,
            args=args,
            headers={"Accept": accept} if accept else None,
        )

    def get_risk_instances(
        self, include_events: Optional[bool] = None, accept: Optional[str] = None
    ) -> dict:
        """Retrieve risk instances.

        Args:
            include_events (bool): Optional; Whether to include events.
            accept (str): Optional; Accept header.

        Returns:
            dict: Risk instances result.
        """
        args = {"includeEvents": include_events}
        return self._get(
            self.risk_instances_path,
            args=args,
            headers={"Accept": accept} if accept else None,
        )

    def patch_risk_instances(self, data: dict) -> dict:
        """Patch risk instances.

        Args:
            data (dict): Risk instances data.

        Returns:
            dict: Risk instances result.
        """
        return self._patch(self.risk_instances_path, data=data)

    def search_risk_instances(self, data: dict, accept: Optional[str] = None) -> dict:
        """Search risk instances.

        Args:
            data (dict): Query data.
            accept (str): Optional; Accept header.

        Returns:
            dict: Risk instances result.
        """
        return self._post(
            f"{self.risk_instances_path}/search",
            data=data,
            headers={"Accept": accept} if accept else None,
        )

    def get_risk_instance(
        self, risk_instance_id: int, include_events: Optional[bool] = None
    ) -> dict:
        """Retrieve a risk instance.

        Args:
            risk_instance_id (int): Risk instance ID.
            include_events (bool): Optional; Whether to include events.

        Returns:
            dict: Risk instance result.
        """
        args = {"includeEvents": include_events}
        return self._get(f"{self.risk_instances_path}/{risk_instance_id}", args=args)

    def patch_risk_instance(self, risk_instance_id: int, data: dict) -> dict:
        """Patch a risk instance.

        Args:
            risk_instance_id (int): Risk instance ID.
            data (dict): Risk instance data.

        Returns:
            dict: Risk instance result.
        """
        return self._patch(f"{self.risk_instances_path}/{risk_instance_id}", data=data)

    def get_risk_types(
        self,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[List[str]] = None,
        include_events: Optional[bool] = None,
        accept: Optional[str] = None,
    ) -> dict:
        """Retrieve risk types.

        Args:
            limit (int, optional): Maximum number of results to return. Defaults to 1000.
            page (int, optional): Page number to begin at when searching. Defaults to 1.
            sort (list): Optional; Sort by field(s).
            include_events (bool): Optional; Whether to include events.
            accept (str): Optional; Accept header.

        Returns:
            dict: Risk types result.
        """
        args: Dict[str, Any] = {"sort": sort, "includeEvents": include_events}
        if page:
            args["page"] = page
        if limit:
            args["limit"] = limit
        return self._get(
            self.risk_types_path,
            args=args,
            headers={"Accept": accept} if accept else None,
        )

    def get_risk_type(
        self, risk_type: str, include_events: Optional[bool] = None
    ) -> dict:
        """Retrieve a risk type.

        Args:
            risk_type (str): Risk type.
            include_events (bool): Optional; Whether to include events.

        Returns:
            dict: Risk type result.
        """
        escaped_risk_type = urllib.parse.quote(risk_type, safe="")
        args = {"includeEvents": include_events}
        return self._get(f"{self.risk_types_path}/{escaped_risk_type}", args=args)

    def patch_risk_type(self, risk_type: str, data: dict) -> dict:
        """Patch a risk type.

        Args:
            risk_type (str): Risk type.
            data (dict): Risk type data.

        Returns:
            dict: Risk type result.
        """
        escaped_risk_type = urllib.parse.quote(risk_type, safe="")
        return self._patch(f"{self.risk_types_path}/{escaped_risk_type}", data=data)
