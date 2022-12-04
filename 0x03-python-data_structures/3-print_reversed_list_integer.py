#!/usr/bin/python3

def print_reversed_list_integer(my_list=None):
    if my_list is None:
        my_list = []
    list_len = len(my_list)
    for i in range(list_len):
        print("{:d}".format(my_list[(list_len-(i+1))]))
