import pandas as pd

data = {
    "student_name": ["Aarav", "Diya", "Ishaan", "Meera", "Rohan"],
    "math_marks": [85, 92, 78, 88, 90],
    "science_marks": [82, 89, 84, 91, 87]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df = df.rename(columns={
    "student_name": "Name",
    "math_marks": "Math",
    "science_marks": "Science"
})

print("\nRenamed columns:")
print(df)

print("\nSorted by Math descending:")
print(df.sort_values(by="Math", ascending=False))

print("\nSorted by Science and Math:")
print(df.sort_values(by=["Science", "Math"], ascending=[False, False]))
