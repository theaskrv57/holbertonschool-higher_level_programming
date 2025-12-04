#!/usr/bin/python3
"""
Uses GitHub API to display your user id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]   # personal access token

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    try:
        data = response.json()
        print(data.get("id"))
    except ValueError:
        print("None")
