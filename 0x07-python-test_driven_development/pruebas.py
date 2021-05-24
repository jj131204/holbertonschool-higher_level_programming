#!/usr/bin/python3

matrix = [

]


for j in matrix:
    for a in j:
        if type(a) is not int and  type(a) is not float:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")



list_1 = []
for i in range(len(matrix)):
        list_1.append(list(map(lambda x: round(x / 3, 3), matrix[i])))


n = len(matrix[0])
j = len(matrix[1])

print(n)
print(j)

print(list_1)


"""

Error cases

    >>> matrix_divided([[4, 3, 2], ["hola", 2, 3]], 3)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix_divided([[1, 2, 3], [1, 2, 3, 4]], 3)
    Traceback (most recent call last):
    TypeError: Each row of the matrix must have the same size

    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero

"""
