#!/usr/bin/python3

"""File reading function"""


def read_file(filename=""):
    """Code here"""
    with open(filename, encoding='utf8') as f:
        print(f.read(), end='')
