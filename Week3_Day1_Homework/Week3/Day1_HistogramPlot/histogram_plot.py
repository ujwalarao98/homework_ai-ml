# Week 3 - Day 1
# Histogram Plot

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
scores = np.random.randint(40, 101, 50)

print("Sample scores:")
print(scores)

plt.hist(scores, bins=6, edgecolor="black")
plt.title("Distribution of Student Scores")
plt.xlabel("Score Range")
plt.ylabel("Number of Students")
plt.show()
