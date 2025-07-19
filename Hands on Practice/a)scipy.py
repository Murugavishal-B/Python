import numpy as np
from scipy.linalg import eig
matrix = np.array([[4, 2], [1, 3]])
eigenvalues, eigenvectors = eig(matrix)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
