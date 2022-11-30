#!/usr/bin/python3
for i in range(0, 9):
    for x in range(0, 10):
        if x == i:
            continue
        elif i == 8 and x == 9:
            print(f'{i:d}{x:d}')
        else:
            print(f'{i:d}{x:d}', end=', ')
