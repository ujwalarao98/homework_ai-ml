# Week 1 - Day 3
# String Operations Practice

def string_length(text):
    return len(text)


def to_uppercase(text):
    return text.upper()


def to_lowercase(text):
    return text.lower()


def reverse_string(text):
    return text[::-1]


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for character in text:
        if character in vowels:
            count += 1

    return count


text = input("Enter a string: ")

print("Length:", string_length(text))
print("Uppercase:", to_uppercase(text))
print("Lowercase:", to_lowercase(text))
print("Reverse:", reverse_string(text))
print("Vowel count:", count_vowels(text))
