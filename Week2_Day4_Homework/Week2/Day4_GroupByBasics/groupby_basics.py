import pandas as pd

data = {
    "Name": ["Aarav", "Diya", "Ishaan", "Meera", "Rohan", "Anaya"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Score": [85, 92, 78, 88, 90, 84]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nCount by department:")
print(df.groupby("Department")["Name"].count())

print("\nAverage score by department:")
print(df.groupby("Department")["Score"].mean())

summary = df.groupby("Department").agg(
    Student_Count=("Name", "count"),
    Average_Score=("Score", "mean")
)

print("\nGrouped summary:")
print(summary)
