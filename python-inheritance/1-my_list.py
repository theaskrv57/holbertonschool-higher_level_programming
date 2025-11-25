#!/usr/bin/python3
"""Module defines a class MyList that inherits from list."""


class MyList(list):
    """MyList inherits from the built-in list class."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original list."""
        print(sorted(self))
