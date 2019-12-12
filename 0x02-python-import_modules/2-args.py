#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(sys.argv) - 1
    if x == 0:
        str1 = "arguments."
    elif x == 1:
        str1 = "argument:"
    else:
        str1 = "arguments:"
    print("{} {}".format(x, str1))
    argv_num = 1
    while x > 0:
        print("{}: {}".format(argv_num, sys.argv[argv_num]))
        x -= 1
        argv_num += 1
