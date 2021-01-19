#!/usr/bin/python3
'''comment'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''son class of BaseGeometry'''

    def __init__(self, width, height):
        '''method of instance'''

        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
