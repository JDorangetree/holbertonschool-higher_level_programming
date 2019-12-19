#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    all_keys = a_dictionary.keys()
    for i in all_keys:
        if i == key:
            del a_dictionary[i]
            return a_dictionary
    return a_dictionary
