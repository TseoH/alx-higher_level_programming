#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is None:
        my_list = []
    new_value = my_list.copy()
    for i in range(len(new_value)):
        if new_value[i] == search:
            new_value[i] = replace
    return new_value
