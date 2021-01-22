#!/usr/bin/python3
'''class Base '''


class Base:
    '''comment'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        method constructor
        count to numbers of id attributes
        '''
        self.id = id

        if self.id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
