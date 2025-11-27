#!/usr/bin/env python3
"""Convert CSV data to JSON format using serialization techniques."""
import csv
import json


def convert_csv_to_json(csv_filename: str) -> bool:
    """
    Convert CSV data to JSON and write to data.json.

    Args:
        csv_filename (str): Input CSV file name.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        # Read CSV file as list of dictionaries
        with open(csv_filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]

        # Write the list of dictionaries as JSON
        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True
    except (FileNotFoundError, IOError, csv.Error, json.JSONDecodeError):
        return False
