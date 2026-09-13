# Week 1 - Day 5
# File Handling Basics

file_name = "practice.txt"

with open(file_name, "w") as file:
    file.write("This is my Week 1 Day 5 file handling practice.\n")
    file.write("Python makes it easy to work with text files.\n")

print("Initial content written successfully.")

with open(file_name, "a") as file:
    file.write("This line was added using append mode.\n")

print("New content appended successfully.")

print("\nFile contents:")
with open(file_name, "r") as file:
    print(file.read())
