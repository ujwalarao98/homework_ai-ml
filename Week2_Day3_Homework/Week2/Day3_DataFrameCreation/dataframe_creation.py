import pandas as pd

student_data = {
    "Name": ["Aarav", "Diya", "Ishaan", "Meera"],
    "Math": [85, 92, 78, 88],
    "Science": [82, 89, 84, 91]
}

df = pd.DataFrame(student_data)

print("DataFrame from dictionary:")
print(df)

print("\nFirst rows:")
print(df.head())

print("\nShape:", df.shape)
print("Columns:", list(df.columns))
print("Rows:", len(df))
print("Columns count:", len(df.columns))

rows = [
    ["Rohan", 90, 87],
    ["Anaya", 76, 81]
]

df2 = pd.DataFrame(rows, columns=["Name", "Math", "Science"])

print("\nDataFrame from list:")
print(df2)
