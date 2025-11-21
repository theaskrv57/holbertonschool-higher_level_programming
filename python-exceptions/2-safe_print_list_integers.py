#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Attempt
            value = my_list[i]

            # Attempt intege
            print("{:d}".format(value), end="")

            count += 1

        except IndexError:
            # Propagate the exception as required
            raise
        except (ValueError, TypeError):
            # Skip silently if not an integer
            continue

    print()
    return count
