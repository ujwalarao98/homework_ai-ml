# Week 2 - Day 2
# Random Number Arrays

import numpy as np

random_integers = np.random.randint(1, 101, size=10)

print("Random integers:")
print(random_integers)
print("Minimum:", random_integers.min())
print("Maximum:", random_integers.max())

random_floats = np.random.random(5)

print("\nRandom floats between 0 and 1:")
print(random_floats)
print("Minimum:", random_floats.min())
print("Maximum:", random_floats.max())

random_2d = np.random.randint(10, 51, size=(3, 4))

print("\n3 x 4 random integer array:")
print(random_2d)
print("Shape:", random_2d.shape)
print("Smallest value:", random_2d.min())
print("Largest value:", random_2d.max())
