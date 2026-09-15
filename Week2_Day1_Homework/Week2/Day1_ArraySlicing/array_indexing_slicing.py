# Week 2 - Day 1
# Array Indexing and Slicing

import numpy as np

array = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("Original Array:")
print(array)

print("\nElement at row 1, column 2:")
print(array[1, 2])

print("\nFirst row:")
print(array[0])

print("\nSecond column:")
print(array[:, 1])

print("\nFirst two rows:")
print(array[0:2])

print("\nSelected rows and columns:")
print(array[1:3, 1:4])
