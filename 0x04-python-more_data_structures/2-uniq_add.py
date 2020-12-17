#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    long = len(uniq)
    res = 0
    print(uniq)
    for i in range(long + 1):
        res = res + i
    return(res)
