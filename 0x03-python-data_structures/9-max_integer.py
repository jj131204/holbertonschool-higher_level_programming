#!/usr/bin/python3
def max_integer(my_list=[]):

    largue = len(my_list)
    if largue == 0:
        return None

    max = my_list[0]
    for j in range(largue):
        if my_list[j] > max:
            max = my_list[j]
    return max
