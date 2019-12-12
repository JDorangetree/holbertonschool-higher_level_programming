#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_argv = len(sys.argv)
    if len_argv == 1:
        sum = 0
    else:
        sum = int(sys.argv[1]) + int(sys.argv[2])
    print("{}".format(sum))
