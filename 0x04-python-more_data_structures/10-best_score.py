#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        list_values = a_dictionary.values()
        x = max(list_values)
        dict_max = {k: v for (k, v) in a_dictionary.items() if v == x}
        list_max = list(dict_max)
        return list_max[0]
    return None
