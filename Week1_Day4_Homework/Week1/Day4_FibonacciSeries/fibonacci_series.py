# Week 1 - Day 4
# Fibonacci Series

# Ask the user how many terms they want.
n = int(input("Enter the number of terms: "))

# The first two Fibonacci numbers.
first = 0
second = 1

print("Fibonacci Series:")

# Repeat the loop N times.
for i in range(n):
    # Print the current Fibonacci number.
    print(first)

    # Find the next number by adding the previous two.
    next_number = first + second

    # Move the values forward for the next loop.
    first = second
    second = next_number

print()
