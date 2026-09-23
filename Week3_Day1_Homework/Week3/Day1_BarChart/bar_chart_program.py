# Week 3 - Day 1
# Bar Chart Program

import matplotlib.pyplot as plt

categories = ["Python", "SQL", "Pandas", "NumPy", "Git"]
hours = [8, 6, 5, 4, 3]

plt.bar(categories, hours)
plt.title("Study Hours by Topic")
plt.xlabel("Topics")
plt.ylabel("Hours")
plt.show()
