#!/usr/bin/python3
# Prints numbers from 0 to 99, two digits, separated by ", "

for i in range(0, 100):
    print("{:02}".format(i), end=", " if i != 99 else "\n")
