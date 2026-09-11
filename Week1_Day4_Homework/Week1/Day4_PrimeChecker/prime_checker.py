# Week 1 - Day 4
# Prime Number Checker

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


# Test with different values
numbers = [2, 7, 10, 13, 20]

for number in numbers:
    if is_prime(number):
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
