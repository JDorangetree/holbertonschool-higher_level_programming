#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename, mode='r', encoding='utf-8') as new_file:
        x = json.load(new_file)
        return x
