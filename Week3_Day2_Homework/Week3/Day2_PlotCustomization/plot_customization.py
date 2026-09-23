# Week 3 - Day 2
# Plot Customization

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6]
temperature = [72, 74, 71, 76, 79, 81]
humidity = [60, 58, 65, 55, 50, 48]

plt.figure(figsize=(9, 5))
plt.plot(days, temperature, marker="o", label="Temperature")
plt.plot(days, humidity, marker="s", label="Humidity")
plt.title("Weather Measurements")
plt.xlabel("Day")
plt.ylabel("Value")
plt.grid(True)
plt.legend()
plt.show()
