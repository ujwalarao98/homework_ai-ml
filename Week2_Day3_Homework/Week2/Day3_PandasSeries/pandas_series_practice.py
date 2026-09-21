import pandas as pd

marks = pd.Series(
    [85, 92, 78, 88, 95],
    index=["Aarav", "Diya", "Ishaan", "Meera", "Rohan"]
)

print("Complete Series:")
print(marks)

print("\nDiya's marks:")
print(marks["Diya"])

print("\nFirst two values:")
print(marks.iloc[0:2])

print("\nMarks greater than 85:")
print(marks[marks > 85])

print("\nNumber of values:", marks.size)
print("Average marks:", marks.mean())
print("Highest marks:", marks.max())
