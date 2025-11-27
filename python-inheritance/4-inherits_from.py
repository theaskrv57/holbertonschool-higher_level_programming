#!/usr/bin/python3


"""salam"""


def inherits_from(obj, a_class):
    """Return True if s;
    otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
