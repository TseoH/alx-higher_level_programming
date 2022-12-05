#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for y in range(len(matrix)):
        i = matrix[y]
        for x in range(len(i)):
            print("{:d}".format(i[x]), end='')
            if x != len(i):
                print(" ".format(i[x]), end='')
        print("")
