# Week 2 - Day 1
# NumPy Array Creation

import numpy as np

array_1d = np.array([10, 20, 30, 40, 50])

print("1D Array:")
print(array_1d)
print("Shape:", array_1d.shape)
print("Size:", array_1d.size)
print("Number of dimensions:", array_1d.ndim)

array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(array_2d)
print("Shape:", array_2d.shape)
print("Size:", array_2d.size)
print("Number of dimensions:", array_2d.ndim)
