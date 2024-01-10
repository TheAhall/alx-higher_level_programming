#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmat = []
    for index in matrix:
        newmat.append([i**2 for i in index])
    return newmat
