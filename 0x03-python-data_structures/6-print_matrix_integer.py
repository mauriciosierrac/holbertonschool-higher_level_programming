#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    end = ""
    for i in range(len(matrix)):
        end = ''
        for j in matrix[i]:
            print('{}{:d}'.format(end, j), end="")
            end = ' '
        print('')
