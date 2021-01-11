#!/usr/bin/python3
'''
this program define that class Rectangle
'''


class Rectangle:
    ''' empty class rectangle '''

    def __init__(self, width=0, height=0):
        ''' function initial'''
        self.height = height
        self.width = width

    @property
    def width(self):
        ''' getter width value'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter width'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''getter height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter height'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
