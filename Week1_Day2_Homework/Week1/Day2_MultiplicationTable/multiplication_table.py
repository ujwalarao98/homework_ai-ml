# Week 1 - Day 2
# Multiplication Table Generator

number = int(input("Enter a number: "))

print("\nMultiplication table for", number)

for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)
