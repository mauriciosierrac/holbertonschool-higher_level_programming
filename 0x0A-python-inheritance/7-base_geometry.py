#!/usr/bin/python3


class BaseGeometry:
    '''super class'''

    def area(self):
        '''this method return a exception message'''

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''that method validate a value parameter'''

        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
