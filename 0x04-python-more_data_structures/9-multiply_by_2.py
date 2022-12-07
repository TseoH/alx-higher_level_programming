#!/usr/bin/python3

def multiply_by_2(a_dictionary=None):
    if a_dictionary is None:
        a_dictionary = {}
    return {k: a_dictionary[k] * 2 for k in a_dictionary}
