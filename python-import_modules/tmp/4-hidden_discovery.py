#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    # Load the compiled .pyc file
    spec = importlib.util.spec_from_file_location("hidden_4", "/tmp/hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Print names that do not start with __, sorted alphabetically
    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)
