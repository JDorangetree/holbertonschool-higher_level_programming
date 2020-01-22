#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as new_file:
        i = 0
        for line in new_file:
            i = i + 1
        new_file.seek(0)
        if nb_lines <= 0:
            strg = new_file.read()
            print(strg, end="")
        elif nb_lines >= i:
            strg = new_file.read()
            print(strg, end="")
        else:
            new_file.seek(0)
            while nb_lines > 0:
                print(new_file.readline(), end="")
                nb_lines = nb_lines - 1
