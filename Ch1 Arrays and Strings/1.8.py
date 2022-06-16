# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to O.

import numpy as np

x = np.array([[1, 2, 3], [0, 5, 6]])            # 2x3 array
y = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,0,14,15],[16,17,18,19,20]])

# Using O(mxn) space as we make a deep copy
def zeroMatrix1(x):
    matrix = np.copy(x)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i,j] == 0:
                x[i,:] = 0
                x[:,j] = 0

    return x

# Using only the extra space to store 0 pairs of i,j
def zeroMatrix2(matrix):
    zeroPairs = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i,j] == 0:
                zeroPairs.append((i,j))
    for pair in zeroPairs:
        i, j = pair[0], pair[1]
        matrix[i,:] = 0
        matrix[:,j] = 0
    return matrix

print(zeroMatrix2(y))


