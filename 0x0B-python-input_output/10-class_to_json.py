#!/usr/bin/python3
def class_to_json(obj):
    if hasattr(obj, "__dict__"):
        return obj.__dict__
