#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    len1 = len(tuple_a)
    len2 = len(tuple_b)

    if len1 > 2:
        len1 = 2

    if len2 > 2:
        len2 = 2

    for i in range(len1):
        a[i] += tuple_a[i]

    for j in range(len2):
        b[j] += tuple_b[j]

    return (a[0] + b[0], a[1] + b[1])
