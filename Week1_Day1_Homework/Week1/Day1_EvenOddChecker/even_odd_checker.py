# Week 1 - Day 1
# Even/Odd Checker
# Takes five numbers as input and checks each number using a function.

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


numbers = []

print("Enter 5 numbers:")

for i in range(5):
    number = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(number)

print("\nResults:")

for number in numbers:
    print(number, "is", check_even_odd(number))
