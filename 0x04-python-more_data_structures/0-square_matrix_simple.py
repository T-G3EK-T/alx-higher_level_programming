#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in range(len(matrix)):
        a = []
        for column in range(len(matrix[0])):
            a.append(matrix[row][column]**2)
        new_matrix.append(a)

