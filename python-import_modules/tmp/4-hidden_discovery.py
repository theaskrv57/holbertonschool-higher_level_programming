#!/usr/bin/python3
import marshal
import sys

if __name__ == "__main__":
    pyc_file = "/tmp/hidden_4.pyc"
    with open(pyc_file, "rb") as f:
        f.read(16)
        code = marshal.load(f)

    names = set()

    def extract_names(code_obj):
        for name in code_obj.co_names:
            if not name.startswith("__"):
                names.add(name)
        for const in code_obj.co_consts:
            if isinstance(const, type(code_obj)):
                extract_names(const)

    extract_names(code)
    for name in sorted(names):
        print(name)
