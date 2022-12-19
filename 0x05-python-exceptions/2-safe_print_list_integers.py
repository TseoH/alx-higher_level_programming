#!/usr/bin/python3

def safe_print_list_integers(my_list=None, x=0):
    if my_list is None:
        my_list = []
    list_len = 0
    for i in range(x):
        try:
            value = int(my_list[i])
            print("{:d}".format(value))
            list_len += 1
        except ValueError:
            continue
        except IndexError:
            break
    return list_len
