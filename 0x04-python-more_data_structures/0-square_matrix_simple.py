#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result = [[0 for _ in range(len(row))] for row in matrix]

    # Iterate through each element in the matrix and compute its square
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Square each element and store it in the corresponding position of the result matrix
            result[i][j] = matrix[i][j] ** 2

    return result
