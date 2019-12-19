#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_list = list(set(set_1) & set(set_2))
    return common_list
