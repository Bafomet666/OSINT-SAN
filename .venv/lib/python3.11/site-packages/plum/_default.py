# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2022 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Default sentinal."""


class NoDefault:

    """Default sentinal."""

    def __new__(cls):
        try:
            instance = NO_DEFAULT
        except NameError:
            instance = super().__new__(cls)

        return instance

    def __repr__(self):
        return "NO_DEFAULT"


NO_DEFAULT = NoDefault()
