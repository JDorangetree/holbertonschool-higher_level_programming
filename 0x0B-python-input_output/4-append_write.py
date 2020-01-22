#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as new_file:
        return(new_file.write(text))
