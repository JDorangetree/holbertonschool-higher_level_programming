#!/usr/bin/python3
""" class that inherits from list"""


class MyList(list):
    """ class that inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        new_list = MyList()
        new_list = self.copy()
        new_list.sort()
        print(new_list)
