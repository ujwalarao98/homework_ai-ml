# Week 2 - Day 2
# Matrix Operations

import numpy as np

matrix_a = np.array([
    [1, 2],
    [3, 4]
])

matrix_b = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

print("\nMatrix addition:")
print(matrix_a + matrix_b)

print("\nElement-wise multiplication:")
print(matrix_a * matrix_b)

print("\nMatrix multiplication:")
print(np.matmul(matrix_a, matrix_b))

print("\nMatrix multiplication using @:")
print(matrix_a @ matrix_b)
