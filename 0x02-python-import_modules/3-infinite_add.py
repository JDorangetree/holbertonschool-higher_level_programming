#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_argv = len(sys.argv)
    if len_argv == 1:
        sum = 0
    else:
        sum = 0
        while len_argv > 1:
            sum = sum + int(sys.argv[len_argv - 1])
            len_argv -= 1
    print("{}".format(sum))
