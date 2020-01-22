#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, encoding='utf-8') as new_file:
        i = 0
        for line in new_file:
            i = i + 1
        return i
