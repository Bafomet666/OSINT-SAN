# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Exception classes."""


class UnpackError(Exception):

    """Unpack error."""

    def __init__(self, dump=None, exception=None):
        message = (
            f"\n\n{dump}\n\n"
            f"{type(exception).__name__} occurred during unpack operation:"
            f"\n\n{exception}"
        )
        Exception.__init__(self, message)


class ExcessMemoryError(UnpackError):

    """Leftover bytes after unpack operation."""

    def __init__(self, extra_bytes=b""):
        # pylint: disable=non-parent-init-called,super-init-not-called
        message = f"{len(extra_bytes)} unconsumed bytes"
        Exception.__init__(self, message)
        self.extra_bytes = extra_bytes


class ImplementationError(Exception):

    """Unexpected implementation error."""

    def __init__(self, message=""):
        if not message:
            message = (
                "One of the plum types used in the pack/unpack operation "
                "contains an implementation error. The operation generated "
                "an exception when first performed without a dump (for efficiency). "
                "But when the operation was repeated with a dump (for a better "
                "exception message) the exception did not re-occur. Please report "
                "the inconsistent behavior to the type developer."
            )
        super().__init__(message)


class InsufficientMemoryError(UnpackError):

    """Too few bytes to unpack an item."""

    def __init__(self, message):
        # pylint: disable=non-parent-init-called,super-init-not-called
        Exception.__init__(self, message)


class PackError(Exception):

    """Pack operation error."""

    def __init__(self, message="", dump=None, exception=None):
        if dump:
            message += f"\n\n{dump}\n\n"

        if exception:
            message += f"{type(exception).__name__} occurred during pack operation:\n\n{exception}"

        Exception.__init__(self, message)


class SizeError(Exception):

    """Size varies from instance to instance."""
