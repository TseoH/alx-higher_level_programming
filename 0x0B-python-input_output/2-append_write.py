#!/usr/bin/python3

"""File append function"""


def append_write(filename="", text=""):
    """Code here"""
    with open(filename, 'a', encoding='utf8')as f:
        return f.write(text)
