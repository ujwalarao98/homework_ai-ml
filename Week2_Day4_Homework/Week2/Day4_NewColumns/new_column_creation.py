import pandas as pd

data = {
    "Name": ["Aarav", "Diya", "Ishaan", "Meera"],
    "Math": [85, 92, 78, 88],
    "Science": [82, 89, 84, 91],
    "English": [90, 86, 80, 93]
}

df = pd.DataFrame(data)

df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3
df["Percentage"] = (df["Total"] / 300) * 100

print("DataFrame with new columns:")
print(df)

print("\nName, Total, Average, Percentage:")
print(df[["Name", "Total", "Average", "Percentage"]])
