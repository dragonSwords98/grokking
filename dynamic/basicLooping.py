
# Contributed by: Bryan Ling

# loop through a 2-D array with numpy to show how to iterate only half the array

import numpy as np

def touchHalf(matrix, x, y):
    s = 0
    while s <= x:
        t = 0
        while t < y - s:
            u = t + s
            matrix[t][u] += 1
            t += 1
        s += 1
    s = 0

    return matrix


def scalarMatrix(matrix, x, k):
    # builds identity matrix if k = 1, otherwise scalar matrix of k

    for i in range(x):
        matrix[i][i] = k

    return matrix

def createMatrix(x, y):
    return np.zeros([x, y])

m = createMatrix(3, 3)
s = scalarMatrix(m, 3, 2)
print(touchHalf(s, 3, 3))
m = createMatrix(1, 1)
print(touchHalf(m, 1, 1))
m = createMatrix(5, 5)
print(touchHalf(m, 5, 5))
m = createMatrix(8, 8)
print(touchHalf(m, 8, 8))
m = createMatrix(10, 10)
s = scalarMatrix(m, 10, 2)
print(touchHalf(s, 10, 10))