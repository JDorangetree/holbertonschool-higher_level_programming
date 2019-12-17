#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        x = my_list[i]
        print("{:d}".format(x))
