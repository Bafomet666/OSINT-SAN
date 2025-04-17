"""Base for interacting with the Censys Search API."""

import os
from typing import List, Optional, Type

from requests.models import Response

from censys.common.base import CensysAPIBase
from censys.common.config import DEFAULT, get_config
from censys.common.exceptions import (
    CensysException,
    CensysExceptionMapper,
    CensysSearchException,
)

Fields = Optional[List[str]]


class CensysSearchAPIv1(CensysAPIBase):
    """This class is the base class for all v1 API indexes."""

    DEFAULT_URL: str = "https://search.censys.io/api/v1"
    """Default Search API base URL."""
    INDEX_NAME: Optional[str] = None
    """Name of Censys Index."""

    def __init__(
        self, api_id: Optional[str] = None, api_secret: Optional[str] = None, **kwargs
    ):
        """Inits CensysSearchAPIv1.

        See CensysAPIBase for additional arguments.

        Args:
            api_id (str): Optional; The API ID provided by Censys.
            api_secret (str): Optional; The API secret provided by Censys.
            **kwargs: Arbitrary keyword arguments.

        Raises:
            CensysException: Base Exception Class for the Censys API.
        """
        CensysAPIBase.__init__(self, kwargs.pop("url", self.DEFAULT_URL), **kwargs)

        # Gets config file
        config = get_config()

        # Try to get credentials
        self._api_id = (
            api_id or os.getenv("CENSYS_API_ID") or config.get(DEFAULT, "api_id")
        )
        self._api_secret = (
            api_secret
            or os.getenv("CENSYS_API_SECRET")
            or config.get(DEFAULT, "api_secret")
        )
        if not self._api_id or not self._api_secret:
            raise CensysException("No API ID or API secret configured.")

        self._session.auth = (self._api_id, self._api_secret)

        # Generate concrete paths to be called
        self.search_path = f"/search/{self.INDEX_NAME}"
        self.view_path = f"/view/{self.INDEX_NAME}/"
        self.report_path = f"/report/{self.INDEX_NAME}"

        # Confirm setup
        # self.account()

    def _get_exception_class(  # type: ignore
        self, res: Response
    ) -> Type[CensysSearchException]:
        return CensysExceptionMapper.SEARCH_EXCEPTIONS.get(
            res.status_code, CensysSearchException
        )

    def account(self) -> dict:
        """Gets the current account information.

        This includes email and quota.

        Returns:
            dict: Account response.
        """
        return self._get("account")

    def quota(self) -> dict:
        """Gets the current account's query quota.

        Returns:
            dict: Quota response.
        """
        return self.account()["quota"]
