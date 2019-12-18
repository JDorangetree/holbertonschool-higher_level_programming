#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return_list = []
    tmp = [True, False]
    for i in my_list:
        if i % 2 == 0:
            return_list.append(tmp[0])
        else:
            return_list.append(tmp[1])
    return return_list
