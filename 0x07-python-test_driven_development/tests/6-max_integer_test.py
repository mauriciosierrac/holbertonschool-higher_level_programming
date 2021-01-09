#!/usr/bin/python3
'''
test Function Max Integer
'''
import unittest

max_integer = __import__('6-max_integer').max_integer


class max_integer_test(unittest.TestCase):
    ''' Test for 6-max_integer Function '''

    def test_max_integer(self):
        '''Tests Cases'''
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer('Hello'), 'o')
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([-8, -50, -10]), -8)
        self.assertEqual(max_integer([0.2, 4.2, 10.3]), 10.3)


if __name__ == '__main__':
    unittest.main()
