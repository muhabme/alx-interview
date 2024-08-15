#!/usr/bin/python3
import sys

total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_stats():
    """ Function to print the current statistics """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        if len(parts) > 6:
            try:
                file_size = int(parts[-1])
                total_size += file_size
            except Exception:
                pass

            status_code = parts[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass

finally:
    print_stats()
