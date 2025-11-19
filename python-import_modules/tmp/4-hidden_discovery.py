#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    # Load the hidden_4.pyc module
    spec = importlib.util.spec_from_file_location("hidden_4", "/tmp/hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Get all names, filter out those starting with '__', sort, and print
    names = dir(hidden_4)
    filtered_names = [name for name in names if not name.startswith("__")]
    for name in sorted(filtered_names):
        print(name)
