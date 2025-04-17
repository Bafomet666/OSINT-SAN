# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Classes and utilities for packing/unpacking bytes."""

import os

enable_boost = os.environ.get("ENABLE_PLUM_BOOST", "AUTO").upper()

"""
if enable_boost in {"AUTO", "YES"}:  # pragma: no cover
    try:
        import plum_boost as boost  # pylint: disable=import-error
    except ModuleNotFoundError:
        if enable_boost == "YES":
            raise
        boost = None
    else:
        pack = data.plum_namespace["pack"] = boost.pack
        unpack = data.plum_namespace["unpack"] = boost.unpack
        data.Data.pack = boost.PackMethod()
        data.Data.unpack = classmethod(boost.unpack)

elif enable_boost == "NO":  # pragma: no cover
    boost = None

else:  # pragma: no cover
    raise RuntimeError(
        "ENABLE_PLUM_BOOST environment variable must be YES, NO, or AUTO"
    )
"""

boost = None

del enable_boost, os
