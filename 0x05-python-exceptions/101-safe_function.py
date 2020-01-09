#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        funct = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
    return funct
