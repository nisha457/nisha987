import numpy as np

# Define two square matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Perform matrix multiplication
result = np.dot(A, B)

# Print the result
print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMultiplication Result (A x B):")
print(result)
