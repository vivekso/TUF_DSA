import numpy as np

# Define the matrix A
# A = np.array([[1, 1, 0, 1],[0, 0, 0, 1],[1, 1, 0, 0]])

# Perform SVD to obtain singular values
# U, s, VT = np.linalg.svd(A)

# Extract the non-zero singular values
# non_zero_singular_values = s[s > 1e-10]

# Display the non-zero singular values
# print("Non-zero singular values:", non_zero_singular_values)



# Define the matrix A
A = np.array([[1, 0, 1, 0],
              [0, 1, 0, 1]])

# Perform SVD
U, s, VT = np.linalg.svd(A)

# Display the U, singular values (s), and VT matrices
print("Matrix U:")
print(U)
print("\nSingular Values (s):")
print(s)
print("\nMatrix VT (conjugate transpose of V):")
print(VT)