#!/usr/bin/python3
'''Function to add 2 integers'''


def add_integer(a, b=98):
    '''
    Add 2 integers

    Return: value of add
    Raise: TypeError if num1 or num2 are not integer or are not float
    '''

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError('a must be an integer')
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
