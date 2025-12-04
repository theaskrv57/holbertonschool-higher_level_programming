#!/usr/bin/python3
"""Compute metrics from stdin logs."""

import sys


def print_stats(total_size, status_codes):
    """Print the accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code]:
            print(f"{code}: {status_codes[code]}")


if __name__ == "__main__":
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) < 2:
                continue

            # Update total file size (last element)
            try:
                size = int(parts[-1])
                total_size += size
            except ValueError:
                pass

            # Update status code (second to last element)
            try:
                code = int(parts[-2])
                if code in status_codes:
                    status_codes[code] += 1
            except ValueError:
                pass

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # On CTRL+C, print stats one last time
        print_stats(total_size, status_codes)
        raise
