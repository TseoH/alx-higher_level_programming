#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding='utf8') as f:
        print(f.read(), end='')
