#!/usr/bin/python3
"""salam"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    status = response.status_code
    if status >= 400:
        print("Error code:", status)
    else:
        print(response.text)
