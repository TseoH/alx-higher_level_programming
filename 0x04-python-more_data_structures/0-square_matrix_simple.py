#!/usr/bin/python3

def square_matrix_simple(matrix=None):
    if matrix is None:
        matrix = []
    return [[i * i for i in x]for x in matrix]
