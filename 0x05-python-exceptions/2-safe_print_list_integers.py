#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if not my_list or x == 0:
        print()
        return (0)
    count = 0
    for i in range(0, x):
        try:
            y = my_list[i]
            print("{:d}".format(y), end="")
        except (ValueError, TypeError):
            pass
        else:
            count = count + 1
    print("")
    return count
