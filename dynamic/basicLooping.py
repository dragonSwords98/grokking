# loop through a 2-D array with numpy to show how to iterate only half the array

import numpy as np

def touchHalf(x, y):
    res = np.zeros([x, y])

    s = 0
    while s < x:
        t = 0
        while t < y - s - 1:
            res[s][t] += 1
            t += 1
        s += 1

    return res


def scalarMatrix(x, k):
    # builds identity matrix if k = 1, otherwise scalar matrix of k

    res = np.zeros([x, x])
    for i in range(x):
        res[i][i] = k

    return res


print(touchHalf(3, 3))
# touchHalf(1, 1)
# touchHalf(5, 5)
# touchHalf(8, 8)
# touchHalf(10, 10)