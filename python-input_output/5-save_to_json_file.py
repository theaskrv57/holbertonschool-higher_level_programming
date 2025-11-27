#!/usr/bin/python3
"""salam"""


import json


def save_to_json_file(my_obj, filename):
    """Write a Python object to a text file as JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
