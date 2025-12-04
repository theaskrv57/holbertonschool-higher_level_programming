#!/usr/bin/python3
"""Module for class_to_json function.
"""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object.

    Args:
        obj: Instance of a class.

    Returns:
        dict: Dictionary representation of the object.
    """
    return obj.__dict__
