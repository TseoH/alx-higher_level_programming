#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

    arg_len = len(argv) - 1

    if arg_len == 0:
        print("{} arguments.".format(arg_len))
    elif arg_len == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(arg_len))
        for i in range(arg_len):
            print("{}: {}".format((i + 1), argv[i + 1]))
