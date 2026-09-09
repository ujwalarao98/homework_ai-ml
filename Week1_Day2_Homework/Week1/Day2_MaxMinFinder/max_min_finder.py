# Week 1 - Day 2
# Find Largest and Smallest
# Finding maximum and minimum manually using loops.
# max() and min() are intentionally NOT used.

numbers = [42, 17, 89, 6, 53, 28, 91, 12]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("Numbers:", numbers)
print("Largest value:", largest)
print("Smallest value:", smallest)
