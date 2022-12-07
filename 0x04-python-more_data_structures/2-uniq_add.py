#!/usr/bin/python3

def uniq_add(my_list=None):
    result = 0
    if my_list is None:
        my_list = []
    new_value = set(my_list.copy())
    for i in new_value:
        result += i
    return result
