# Week 1 - Day 5
# Mini Practice Set

# Problem 1: Count even and odd numbers
numbers = [10, 7, 4, 9, 12, 15, 18]

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Problem 1")
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

# Problem 2: Palindrome using a function and loop
def is_palindrome(word):
    reversed_word = ""

    for character in word:
        reversed_word = character + reversed_word

    return word.lower() == reversed_word.lower()

print("\nProblem 2")
word = "level"

if is_palindrome(word):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")

# Problem 3: Character frequency using a dictionary
print("\nProblem 3")

text = "python"
frequency = {}

for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

for character, count in frequency.items():
    print(character, "->", count)
