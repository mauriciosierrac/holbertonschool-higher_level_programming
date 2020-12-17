#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        powN = list(map(lambda j: j * j, i))
        new.append(powN)
    return (new)
