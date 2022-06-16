import numpy as np

# Create 2 x 3 array (n x m)
A = np.array([[1,2,3],[4,5,6]])
print(A)
# Create 4 x 5 array (n x m)
B = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
print(B)

# Access element in 2nd row and 3rd column
print(A[1,2])

# Access entire 2nd column 
print(A[:,1])

# Access entire 2nd row
print(A[1])

# Get shape of matrix
print(A.shape)

# Get number of rows in matrix
print(A.shape[0])

# Get number of columns in matrix
print(A.shape[1])

# Get every row after the first row
print(B[1:,:])

# Get every element besides first row and column
print(B[1:, 1:])