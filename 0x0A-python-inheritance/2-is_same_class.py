#!/usr/bin/python3
''' comment ''''


def is_same_class(obj, a_class):
    '''
    that function return true or false if this object
    is a class instance
    '''
    if obj.__class__ == a_class:
        return True
    return False
