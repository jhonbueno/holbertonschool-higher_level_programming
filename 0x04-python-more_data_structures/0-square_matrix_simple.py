#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_matrix = matrix.copy()
    for i in range(len(sqr_matrix)):
        for j in range(len(sqr_matrix[i])):
            sqr_matrix[i][j] = sqr_matrix[i][j] ** 2
    return sqr_matrix
