#!/usr/bin/python3
''' class square defines a square by 1-square.py'''


class Square:
    ''' the method validate is size is a integer and calculate square value of size '''

    def __init__(self, size=0):
        '''documentation'''
        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')

        if self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        '''documentation'''
        return (self.__size ** 2)
