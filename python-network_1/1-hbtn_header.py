#!/usr/bin/python3
"""
1-hbtn_header.py

This script takes in a URL, sends a request to the URL, and displays the
value of the X-Request-Id variable found in the header of the response.
"""

import sys
import urllib.request


def main():
    """Main function to get X-Request-Id from URL."""
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader("X-Request-Id")
        print(x_request_id)


if __name__ == "__main__":
    main()
