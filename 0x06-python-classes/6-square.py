#!/usr/bin/python3
''' class square defines a square by 1-square.py'''


class Square():
    ''' the method validate is size is a integer and calculate square value '''

    def __init__(self, size=0, position=(0, 0)):
        '''documentation'''
        self.__size = size
        self.__position = position

    def area(self):
        '''documentation'''
        if type(self.__size) is not int:
            raise TypeError('size must be an integer')
        return self.__size ** 2

    def my_print(self):
        '''documentation'''
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print("{}".format((' ' * self.__position[0] + '#' * self.__size)))

    @property
    def position(self):
        '''documentation'''
        return self.__position

    @position.setter
    def position(self, value):
        '''documentation'''
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or value[0] < 0 or
                type(value[1]) is not int or value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    @property
    def size(self):
        '''documentation'''
        return self.__size

    @size.setter
    def size(self, value):
        '''documentation'''
        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')
