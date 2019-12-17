#!/usr/bin/python3
def no_c(my_string):
    slist = []
    for i in range(0, len(my_string)):
        slist.append(my_string[i])
    for j in slist:
        if j == 'c' or j == 'C':
            slist.remove(j)
    new_string = "".join(slist)
    return new_string
