# Week 1 - Day 3
# Word Counter

sentence = input("Enter a sentence: ")

words = sentence.split()

print(words)
print("Number of words:", len(words))

for word in words:
    print(word, "->", len(word))
