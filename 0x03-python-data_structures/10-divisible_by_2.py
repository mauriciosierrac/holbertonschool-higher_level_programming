#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    resul = []
    if my_list:
        for i in my_list:
            if i % 2 == 0:
                resul.append(True)
            else:
                resul.append(False)
        return (resul)
