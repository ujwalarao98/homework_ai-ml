# Week 1 - Day 1
# Number Classification Program
# Checks whether numbers are positive, negative, or zero.

test_numbers = [10, -7, 0, 25, -3]

for number in test_numbers:
    if number > 0:
        print(number, "is Positive")
    elif number < 0:
        print(number, "is Negative")
    else:
        print(number, "is Zero")
