# Week 1 - Day 3
# Palindrome Checker

word = input("Enter a word: ")

reversed_word = ""

# Reverse the word manually
for character in word:
    reversed_word = character + reversed_word

print("Reversed word:", reversed_word)

if word.lower() == reversed_word.lower():
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
