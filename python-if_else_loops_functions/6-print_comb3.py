#!/usr/bin/python3
# Prints all possible different combinations of two digits

for i in range(0, 10):
    for j in range(i + 1, 10):
        print("{}{}".format(i, j), end=", " if i != 8 or j != 9 else "\n")
