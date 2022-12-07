#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    as_list = list(a_dictionary)
    if len(as_list) == 0:
        return None
    current_key = as_list[0]
    result = a_dictionary[current_key]
    for k, v in a_dictionary.items():
        if v > result:
            result = v
            current_key = k
    return current_key
