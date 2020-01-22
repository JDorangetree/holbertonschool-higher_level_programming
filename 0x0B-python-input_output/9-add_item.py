#!/usr/bin/python3
import json
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        j_list = load_from_json_file("add_item.json")
    except:
        j_list = []

    for i in range(1, len(sys.argv)):
        j_list.append(sys.argv[i])
    save_to_json_file(j_list, "add_item.json")
