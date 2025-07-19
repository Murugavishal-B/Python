import numpy as np
matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
matrix2 = np.array([[7, 8, 9], [10, 11, 12]])
matrix3 = np.array([[1, 2], [3, 4], [5, 6]])
matrix4 = np.array([[7, 8], [9, 10]])
print("Matrix Addition Result:\n", np.add(matrix1, matrix2))
print("Matrix Multiplication Result:\n", np.dot(matrix3, matrix4))
