# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. (an you do this in place?

import numpy as np

matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
A = np.array(matrix)

print(A)


# Not in place - takes O(n^2) space
# Approach: the 0th row becomes the nth column, then 2nd row becomes the n-1th column
def rotateMatrix1(matrix):
    n=len(matrix)
    newMatrix = np.array([[0]*5]*5)
    for i in range(n):
        newMatrix[:, n-i-1] = matrix[i,:]
        # print(matrix[:,n-i-1])
    print(newMatrix)


# Better - takes O(n) space - i think
# def rotateMatrix2(matrix):
#     x=len(matrix)
#     n=len(matrix)
#     for i in range(n):
#         temp = 
#         print(temp)


rotateMatrix1(A)
