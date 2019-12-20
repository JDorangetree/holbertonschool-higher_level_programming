#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        list_values = a_dictionary.values()
        x = max(list_values)
        dict_max = {k: v for (k, v) in a_dictionary.items() if v == x}
        return dict_max.keys()
    return None
