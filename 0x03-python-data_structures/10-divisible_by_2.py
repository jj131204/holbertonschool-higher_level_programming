#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    largue = len(my_list)
    multiples = []
    for i in range(largue):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return multiples
