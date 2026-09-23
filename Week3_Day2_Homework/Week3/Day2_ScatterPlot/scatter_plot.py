# Week 3 - Day 2
# Scatter Plot

import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [48, 55, 61, 68, 72, 80, 86, 93]

plt.scatter(study_hours, scores)
plt.title("Study Hours vs Test Scores")
plt.xlabel("Study Hours")
plt.ylabel("Test Score")
plt.show()
