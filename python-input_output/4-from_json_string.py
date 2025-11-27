#!/usr/bin/python3
"""salam"""


import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string."""
    return json.loads(my_str)
