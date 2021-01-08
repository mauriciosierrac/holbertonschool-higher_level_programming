#!/usr/bin/python3
'''Function divide a matrix'''


def matrix_divided(matrix, div):
    '''
    divide the list on de matrix
    
    Raise: TyperError
    Rerturn: new matrix
    '''
    if (type(matrix) is not list and len(matrix) == 0):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    
    for row in matrix:
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        
    for row in matrix:
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    new = []
    cont1 = 0
    cont2 = 0
    
    for i in matrix:
        res = (list(map(lambda j: round((j / div),2), i)))
        new.append(res)
    return new
