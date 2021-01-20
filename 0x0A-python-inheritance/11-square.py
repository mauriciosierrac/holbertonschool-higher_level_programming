#!/usr/bin/python3
'''comment'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''son class of rectangle'''

    def __init__(self, size):
        '''comment'''
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        ''' print a informal representation of square'''
        return '[Square] {}/{}'.format(self.__size, self.__size)
