import pandas as pd
from pathlib import Path

file_path = Path(__file__).with_name("student_marks.csv")
df = pd.read_csv(file_path)

print("Original dataset:")
print(df)

print("\nMissing values:")
print(df.isnull().sum())

# Fill missing marks with each column's mean.
for column in ["Math", "Science", "English"]:
    df[column] = df[column].fillna(df[column].mean())

print("\nCleaned dataset:")
print(df)

# Create summary columns.
df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(get_grade)

print("\nWith Total, Average, and Grade:")
print(df)

print("\nSummary statistics:")
print(df[["Math", "Science", "English", "Total", "Average"]].describe())

print("\nAverage by department:")
print(df.groupby("Department")["Average"].mean())

print("\nTop student:")
print(df.loc[df["Average"].idxmax(), ["Name", "Average", "Grade"]])

output_path = Path(__file__).with_name("cleaned_student_marks.csv")
df.to_csv(output_path, index=False)

print("\nSaved cleaned file as:", output_path.name)
