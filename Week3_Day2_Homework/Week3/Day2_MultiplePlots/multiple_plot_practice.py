# Week 3 - Day 2
# Multiple Plot Practice

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 135, 180, 210]

# Chart 1: Line chart - shows change over time.
plt.figure()
plt.plot(months, sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

products = ["A", "B", "C", "D"]
units_sold = [50, 75, 45, 90]

# Chart 2: Bar chart - compares categories.
plt.figure()
plt.bar(products, units_sold)
plt.title("Units Sold by Product")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.show()

scores = [45, 50, 55, 58, 60, 61, 65, 70, 72, 75, 80, 82, 85, 90, 95]

# Chart 3: Histogram - shows a distribution.
plt.figure()
plt.hist(scores, bins=5, edgecolor="black")
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()
