#!/usr/bin/python3

"""File writing function"""


def write_file(filename="", text=""):
    """Code here"""
    with open(filename, 'w', encoding='utf8') as f:
        f.write(text)
