#!/usr/bin/python3

"""File json function"""

import json


def load_from_json_file(filename):
    """Code here"""
    with open(filename, encoding='utf8') as f:
        return json.load(f)
