#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    
    for i in range(list_length):
        resul = 0
        
        try:
            resul = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print('Wrong type')
        except ZeroDivisionError:
            print('division by 0')
        except IndexError:
            print('out of range')
        finally:
            new_list.append(resul)
    return (new_list)
