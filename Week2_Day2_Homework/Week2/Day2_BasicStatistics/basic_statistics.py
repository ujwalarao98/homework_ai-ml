# Week 2 - Day 2
# Mean, Median, and Standard Deviation

import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Numbers:")
print(numbers)

numpy_mean = np.mean(numbers)
numpy_median = np.median(numbers)
numpy_std = np.std(numbers)

print("\nUsing NumPy:")
print("Mean:", numpy_mean)
print("Median:", numpy_median)
print("Standard deviation:", numpy_std)

manual_mean = sum(numbers) / len(numbers)

print("\nManual mean:")
print(manual_mean)

middle_index = len(numbers) // 2
manual_median = numbers[middle_index]

print("\nManual median:")
print(manual_median)

squared_differences = []

for number in numbers:
    difference = number - manual_mean
    squared_differences.append(difference ** 2)

variance = sum(squared_differences) / len(numbers)
manual_std = variance ** 0.5

print("\nManual standard deviation:")
print(manual_std)
