#!/usr/bin/python3
for i in range(0, 9):
    for x in range(0, 10):
        if x == i or i > 0 and x == 0:
            continue
        elif i == 8 and x == 9:
            print('{:d}{:d}'.format(i, x))
        else:
            print('{:d}{:d}'.format(i, x), end=', ')
