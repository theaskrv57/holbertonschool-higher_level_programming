#!/usr/bin/python3

"""salam"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    x = response.headers.get("X-Request-Id")
    print(x)
