#!/usr/bin/python3
# def uppercase(str):

def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            i = chr(ord(i) - 32)
        print(f'{i}', end='')
