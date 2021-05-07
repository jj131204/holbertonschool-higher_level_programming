#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for j in matrix:
        new.append(list(map(lambda num: num * num, j)))

    return new
