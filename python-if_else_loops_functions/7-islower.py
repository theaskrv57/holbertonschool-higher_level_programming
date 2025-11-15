#!/usr/bin/python3

def islower(c):
    """
    Returns True if c is a lowercase character, False otherwise.
    """
    if len(c) != 1:
        return False
    return 'a' <= c <= 'z'
