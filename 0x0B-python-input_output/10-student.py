#!/usr/bin/python3
'''comment'''


class Student:
    '''
    class that define a student'''

    def __init__(self, first_name, last_name, age):
        '''instance to class Student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''return a representation of diccionary'''
        if attrs is None:
            return self.__dict__
        new = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new[key] = value
        return new
