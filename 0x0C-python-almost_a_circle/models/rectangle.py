#!/usr/bin/python3
'''define class Rectangle'''
from models.base import Base
import sys


class Rectangle(Base):
    '''Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''getter method'''
        return self.__width

    @property
    def height(self):
        '''getter method'''
        return self.__height

    @property
    def x(self):
        '''Getter method'''
        return self.__x

    @property
    def y(self):
        '''Getter method'''
        return self.__y

    @width.setter
    def width(self, value):
        '''setter method'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        '''setter method'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        '''getter method'''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be > 0')
        self.__x = value

    @y.setter
    def y(self, value):
        '''getter method'''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be > 0')
        self.__y = value

    def area(self):
        '''calculate area'''
        return self.__width * self.__height

    def display(self):
        '''print rectangle with # char'''
        print('\n' * self.__y, end="")
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            print('{}'.format('#') * self.__width)

    def __str__(self):
        '''print the formal representation'''
        '''REDUCIR ESTA LINEA PORQUE MOLESTA EL PEP8'''
        vid = self.id
        vx = self.__x
        vy = self.__y
        vw = self.__width
        vh = self.__height
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(vid, vx, vy, vw, vh))

    def update(self, *args, **kwargs):
        '''method with no keyword arguments'''
        new = ['id', 'width', 'height', 'x', 'y']
        var = 0
        if args and len(args) != 0:
            for i in args:
                if var == 0:
                    super().__init__(i)
                elif var < len(args):
                    setattr(self, new[var], i)
                var += 1
        elif kwargs:
            for key, value in kwargs.items():
                str = 'self.' + key
                exec(str + '= value')

    def to_dictionary(self):
        '''return the representation of dict'''
        vid = self.id
        vx = self.__x
        vy = self.__y
        vw = self.__width
        vh = self.__height
        return {'id': vid, 'widht': vw, 'height': vh, 'x': vx, 'y': vy}
