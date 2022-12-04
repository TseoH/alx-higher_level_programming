#!/usr/bin/python3

def max_integer(my_list=None):
    bigger = None
    if my_list is None:
        my_list = []
    if len(my_list) == 0:
        return bigger
    bigger = 0
    for i in my_list:
        if bigger < i:
            bigger = i
    return bigger
