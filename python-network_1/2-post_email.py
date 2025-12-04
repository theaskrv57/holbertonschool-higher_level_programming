#!/usr/bin/python3
"""
2-post_email.py

This script takes in a URL and an email, sends a POST request to the URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8).

Usage:
    ./2-post_email.py <URL> <email>
"""

import sys
import urllib.request
import urllib.parse


def main():
    """Main function to send POST request with email and print response."""
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode POST data
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Create request object
    req = urllib.request.Request(url, data=data, method='POST')

    # Send request and read response
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))


if __name__ == "__main__":
    main()
