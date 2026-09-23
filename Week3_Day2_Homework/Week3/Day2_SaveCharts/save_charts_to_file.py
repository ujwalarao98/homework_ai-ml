# Week 3 - Day 2
# Save Charts to File

import matplotlib.pyplot as plt
from pathlib import Path

categories = ["Books", "Clothes", "Food", "Travel"]
spending = [120, 250, 300, 180]

plt.bar(categories, spending)
plt.title("Monthly Spending")
plt.xlabel("Category")
plt.ylabel("Amount")

output_file = Path(__file__).with_name("monthly_spending_chart.png")
plt.savefig(output_file, dpi=300, bbox_inches="tight")

print("Chart saved to:")
print(output_file)
plt.show()
