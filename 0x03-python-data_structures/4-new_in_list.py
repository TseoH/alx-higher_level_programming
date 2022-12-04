#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    cloned = my_list[:]
    if idx is None or idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    cloned[idx] = element
    return cloned
