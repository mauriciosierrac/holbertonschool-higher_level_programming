#!/usr/bin/python3
'''define class Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''getter method'''
        return self.__width

    @width.setter
    def width(self, width):
        '''setter method'''
        self.__width = width

    @property
    def height(self):
        '''getter method'''
        return self.__height

    @height.setter
    def height(self, height):
        '''setter method'''
        self.__height = height

    @property
    def x(self):
        '''setter method'''
        return self.__x

    @x.setter
    def x(self, x):
        '''getter method'''
        self.__x = x

    @property
    def y(self):
        '''setter method'''
        return self.__y

    @y.setter
    def y(self, y):
        '''getter method'''
        self.__y = y
