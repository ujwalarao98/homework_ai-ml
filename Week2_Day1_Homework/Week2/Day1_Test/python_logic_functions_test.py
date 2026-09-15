# Week 2 - Day 1
# Test: Python Logic and Functions

# Problem 1: Count vowels in a string
def count_vowels(text):
    count = 0
    for character in text:
        if character.lower() in "aeiou":
            count += 1
    return count

word = "Programming"
print("Problem 1 - Vowel Count")
print("Word:", word)
print("Number of vowels:", count_vowels(word))


# Problem 2: Find even numbers in a list
def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

numbers = [4, 7, 10, 13, 16, 21]
print("\nProblem 2 - Even Numbers")
print("Original list:", numbers)
print("Even numbers:", get_even_numbers(numbers))


# Problem 3: Find the largest number in a list
def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

values = [12, 45, 7, 89, 34]
print("\nProblem 3 - Largest Number")
print("Numbers:", values)
print("Largest number:", find_largest(values))


# Problem 4: Reverse a string manually
def reverse_text(text):
    reversed_text = ""
    for character in text:
        reversed_text = character + reversed_text
    return reversed_text

text = "Python"
print("\nProblem 4 - Reverse String")
print("Original:", text)
print("Reversed:", reverse_text(text))


# Problem 5: Calculate the sum of a list
def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

scores = [10, 20, 30, 40, 50]
print("\nProblem 5 - Sum of List")
print("Numbers:", scores)
print("Total:", calculate_sum(scores))
