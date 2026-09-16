# Week 2 - Day 2
# Reshape and Flatten

import numpy as np

array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print("Original 1D array:")
print(array_1d)
print("Shape:", array_1d.shape)

array_2d = array_1d.reshape(3, 4)

print("\nReshaped 3 x 4 array:")
print(array_2d)
print("Shape:", array_2d.shape)

array_2x6 = array_1d.reshape(2, 6)

print("\nReshaped 2 x 6 array:")
print(array_2x6)
print("Shape:", array_2x6.shape)

flattened_array = array_2d.flatten()

print("\nFlattened array:")
print(flattened_array)
print("Shape:", flattened_array.shape)
