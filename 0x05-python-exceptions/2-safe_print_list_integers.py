#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                cont = cont + 1
                print('{}'.format(my_list[i]), end="")
    except (ValueError, TypeError):
        return

    print()
    return (cont)
