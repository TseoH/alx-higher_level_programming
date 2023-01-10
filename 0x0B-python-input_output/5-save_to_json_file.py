#!/usr/bin/python3

"""File json function"""

import json


def save_to_json_file(my_obj, filename):
    """Code here"""
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(my_obj, f)
