"""Interact with the Censys Seeds, Assets, and Logbook APIs."""

from typing import Optional

from .assets import (
    CertificatesAssets,
    DomainsAssets,
    HostsAssets,
    ObjectStoragesAssets,
    SubdomainsAssets,
    WebEntitiesAssets,
)
from .beta import Beta
from .clouds import Clouds
from .inventory import InventorySearch
from .logbook import Logbook
from .risks import Risks
from .saved_queries import SavedQueries
from .seeds import Seeds


class AsmClient:
    """Client ASM API class."""

    def __init__(self, api_key: Optional[str] = None, **kwargs):
        """Inits AsmClient.

        Args:
            api_key (str): Optional; The API Key provided by Censys.
            **kwargs: Arbitrary keyword arguments.
        """
        self.seeds = Seeds(api_key, **kwargs)
        self.hosts = HostsAssets(api_key, **kwargs)
        self.certificates = CertificatesAssets(api_key, **kwargs)
        self.domains = DomainsAssets(api_key, **kwargs)
        self.subdomains = SubdomainsAssets(api_key, **kwargs)
        self.logbook = Logbook(api_key, **kwargs)
        self.events = self.logbook
        self.clouds = Clouds(api_key, **kwargs)
        self.risks = Risks(api_key, **kwargs)
        self.inventory = InventorySearch(api_key, **kwargs)
        self.object_storages = ObjectStoragesAssets(api_key, **kwargs)
        self.web_entities = WebEntitiesAssets(api_key, **kwargs)
        self.beta = Beta(api_key, **kwargs)
        self.saved_queries = SavedQueries(api_key, **kwargs)
