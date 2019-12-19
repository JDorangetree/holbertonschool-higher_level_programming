#!/usr/bin/python3
def uniq_add(my_list=[]):
    add_list = []
    if my_list:
        for x in my_list:
            if x not in add_list:
                add_list.append(x)
    return sum(add_list)
