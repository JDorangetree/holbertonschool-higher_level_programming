#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    dictionary_keys = a_dictionary.keys()
    for i in dictionary_keys:
        if i == key:
            a_dictionary[i] = value
            return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
