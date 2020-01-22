#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    with open(filename, mode='w', encoding='utf-8') as new_file:
        json.dump(my_obj, new_file)
