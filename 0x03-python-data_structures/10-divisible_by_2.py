#!/usr/bin/python3

def divisible_by_2(my_list=None):
    result = []
    if my_list is None:
        my_list = []
    if len(my_list) == 0:
        return []
    for i in my_list:
        value = i % 2 == 0
        result.append(value)
    return result
