#!/usr/bin/python3

def element_at(my_list, idx):
    if idx is None or idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
