# Week 1 - Day 1
# Test: Python Basics
# Covers variables, data types, input/output, if-else, loops, and functions.

# 1. Variables and data types
name = "Rachana"
age = 25
height = 5.4
is_learning_python = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Learning Python:", is_learning_python)

print("\nData Types:")
print("name ->", type(name))
print("age ->", type(age))
print("height ->", type(height))
print("is_learning_python ->", type(is_learning_python))


# 2. Input / Output
number = int(input("\nEnter a number: "))
print("You entered:", number)


# 3. If-Else
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# 4. Loop
print("\nNumbers from 1 to 5:")
for i in range(1, 6):
    print(i)


# 5. Function
def square(num):
    return num * num


print("\nSquare of", number, "is", square(number))
