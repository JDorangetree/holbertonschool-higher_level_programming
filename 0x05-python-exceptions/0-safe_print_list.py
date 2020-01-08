#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(0, x):
            y = my_list[i]
            print("{}".format(y), end="")
        print("")
        return x
    except IndexError:
        print("")
        return i
