#!/usr/bin/python3

def safe_print_list(my_list=None, x=0):
    if my_list is None:
        my_list = []
    list_len = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            list_len += 1
        except:
            break
    print("")
    return list_len
