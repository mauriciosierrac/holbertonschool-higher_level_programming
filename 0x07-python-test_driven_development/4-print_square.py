#!/usr/bin/python3
''' That function print the square '''


def print_square(size):
    ''' 
    the method validate is size is a integer and calculate square value
    
    Return: Print te square
    '''
    
    
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if type(size) is float:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print('{}'.format("#" * size))
