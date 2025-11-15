#!/usr/bin/python3
# Prints the ASCII alphabet in lowercase, without q and e, without newline

for i in range(97, 123):
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end="")
