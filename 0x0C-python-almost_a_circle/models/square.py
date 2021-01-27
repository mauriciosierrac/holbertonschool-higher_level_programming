#!/usr/bin/python3
'''class square, son of Rectangle'''
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    '''class Square'''

    def __init__(self, size, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''print a formal representation'''
        vid = self.id
        vx = self._Rectangle__x
        vy = self._Rectangle__y
        vw = self._Rectangle__width
        return ('[Square] (' + str(vid) + ') ' + str(vx) +
                '/' + str(vy) + ' - ' + str(vw))

    @property
    def size(self):
        '''getter method of size'''
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        '''setter method'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        self._Rectangle__width = value
        self._Rectangle__height = value

    def update(self, *args, **kwargs):
        '''arguments'''
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self._Rectangle__x = args[2]
            if len(args) >= 4:
                self._Rectangle__y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

        def to_dictionary(self):
            '''return the representation of dict'''
            vid = self.id
            vx = self._Rectangle__x
            vy = self._Rectangle__y
            vs = self.size
            return {'id': vid, 'size': vs, 'x': vx, 'y': vy}
