"""Interact with the Censys Assets API."""

from .assets import Assets
from .certificates import CertificatesAssets
from .domains import DomainsAssets
from .hosts import HostsAssets
from .object_storages import ObjectStoragesAssets
from .subdomains import SubdomainsAssets
from .web_entities import WebEntitiesAssets

__all__ = [
    "Assets",
    "CertificatesAssets",
    "DomainsAssets",
    "HostsAssets",
    "ObjectStoragesAssets",
    "SubdomainsAssets",
    "WebEntitiesAssets",
]
