#!/usr/bin/python3
"""Defines MyList class."""


class MyList(list):
    """Inherits from list."""

    def print_sorted(self):
        """Prints sorted list."""
        print(sorted(self))
