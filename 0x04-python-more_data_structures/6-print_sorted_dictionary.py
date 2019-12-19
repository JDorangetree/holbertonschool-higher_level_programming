#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_of_keys = a_dictionary.keys()
    list_of_keys_sorted = sorted(list_of_keys)
    for i in list_of_keys_sorted:
        print("{}: {}".format(i, a_dictionary[i]))
