#!/usr/bin/env python3
"""Basic serialization module: serialize Python dict to JSON file and deserialize it back."""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): Python dictionary to serialize.
        filename (str): Output JSON file name. Replaces file if it exists.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it into a Python dictionary.

    Args:
        filename (str): Input JSON file name.

    Returns:
        dict: Python dictionary with deserialized JSON data.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
