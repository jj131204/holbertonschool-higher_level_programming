#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    lista = my_list.copy()
    if idx >= 0 and idx < len(my_list):
        lista[idx] = element
    return lista
