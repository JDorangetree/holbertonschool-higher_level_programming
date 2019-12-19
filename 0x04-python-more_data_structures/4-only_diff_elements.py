#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    common_list = list(set(set_1) & set(set_2))
    set_1.update(set_2)
    for i in common_list:
        set_1.remove(i)
    return set_1
