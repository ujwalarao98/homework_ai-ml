# Week 1 - Day 4
# Pattern Printing
# Three star-pattern programs using nested loops.

rows = 5

# Pattern 1: Increasing triangle
print("Pattern 1:")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# Pattern 2: Decreasing triangle
print("\nPattern 2:")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# Pattern 3: Pyramid
print("\nPattern 3:")
for i in range(1, rows + 1):

    # Print spaces before the stars.
    for space in range(rows - i):
        print(" ", end=" ")

    # Print stars.
    for star in range(2 * i - 1):
        print("*", end=" ")

    print()
