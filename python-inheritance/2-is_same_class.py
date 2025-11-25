#!/usr/bin/python3
"""Function that returns True if an object is exactly an instance of a specified class"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, else False."""
    return type(obj) == a_class
