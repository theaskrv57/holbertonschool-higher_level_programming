#!/usr/bin/python3
"""salam"""


def write_file(filename="", text=""):
    """Wrir of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
