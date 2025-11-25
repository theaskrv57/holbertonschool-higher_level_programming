#!/usr/bin/python3
"""Module that defines a MyList class inherited from list."""

class MyList(list):
    """MyList class inherits from list and adds a print_sorted method."""

    def print_sorted(self):
        """Prints the list, but sorted in ascending order."""
        print(sorted(self))
