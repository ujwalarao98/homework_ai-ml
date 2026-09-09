# Week 1 - Day 2
# Sum and Average Program
# Functions are used to keep the code organized.

def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    total = calculate_sum(numbers)
    average = total / len(numbers)

    return average


numbers = [10, 20, 30, 40, 50]

total = calculate_sum(numbers)
average = calculate_average(numbers)

print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)
