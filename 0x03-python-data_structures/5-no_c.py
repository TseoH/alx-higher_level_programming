#!/usr/bin/python3

def no_c(my_string):
    new_string = ''
    if len(my_string) == 0:
        return new_string
    for c in my_string:
        if c != 'c' and c != 'C':
            new_string += c
    return new_string
