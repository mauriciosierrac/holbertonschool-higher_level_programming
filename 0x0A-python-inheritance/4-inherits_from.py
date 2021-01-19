#!/usr/bin/python3
def inherits_from(obj, a_class):
    '''
    that function return true if the object is a instance
    from inheritance class
    '''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
