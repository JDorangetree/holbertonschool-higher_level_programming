#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding='utf-8') as new_file:
        print(new_file.read())
