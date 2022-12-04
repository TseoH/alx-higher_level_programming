#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for y in range(len(matrix)):
        i = matrix[y]
        for x in range(len(i)):
            if x == len(i)-1:
                print("{:d}".format(i[x]), end='')
            else:
                print("{:d} ".format(i[x]), end='')
        if y < len(matrix) - 1:
            print('\n', end='')
