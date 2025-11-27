#!/usr/bin/python3
"""salam"""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
