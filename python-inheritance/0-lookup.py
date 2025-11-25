#!/usr/bin/python3
"""
This module contains the function `lookup` that returns
a list of available attributes and methods of an object.
"""

def lookup(obj):
    """Returns a list of available attributes and methods of obj."""
    return dir(obj)
