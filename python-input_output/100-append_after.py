#!/usr/bin/python3
"""Module that inserts
 a line of text after lines containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a fi
le after each line containing a specific string.

    Args:
        filename (str): Path to the file.
        search_string (str): String to search for in lines.
        new_string (str): String to insert after matching lines.
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if search_string in line:
            new_lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
