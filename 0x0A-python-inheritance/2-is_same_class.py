#!/usr/bin/python3
def is_same_class(obj, a_class):
    """returns True if the object is exactly an\
instance of the specified class"""
    b = a_class()
    if type(b) == type(obj):
        return True
    else:
        return False
