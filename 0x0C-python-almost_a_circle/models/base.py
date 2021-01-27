#!/usr/bin/python3
'''class Base '''
import json
from os import path


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''return representation of Json'''
        if not list_dictionaries or list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''export file'''
        newfile = cls.__name__+'.json'
        newdict = []
        if list_objs is not None:
            for i in list_objs:
                newdict.append(cls.to_dictionary(i))
        with open(newfile, 'w') as file:
            file.write(cls.to_json_string(newdict))

    @staticmethod
    def from_json_string(json_string):
        '''return a representation of Json string'''
        if not json_string or json_string is None:
            return '[]'
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''return a instance with attributes'''
        if cls.__name__ == 'Rectangle':
            new_ins = cls(1, 1)
        else:
            new_ins = cls(1)
        cls.update(new_ins, **dictionary)
        return new_ins

    @classmethod
    def load_from_file(cls):
        '''return a instance list'''
        filename = cls.__name__ + '.json'
        if path.isfile(filename):
            with open(filename, 'r') as f:
                new_list = cls.from_json_string(f.read())
            return [cls.create(**obj) for obj in new_list]
        return []
