#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in x:
            print("{}".format(y) , end=' ')
        print("\n")
