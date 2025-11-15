#!/usr/bin/python3
for i in range(26):
    print("{:c}".format((122 - i) if i % 2 == 0 else (122 - i) - 32), end="")
