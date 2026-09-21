import pandas as pd

data = {
    "Name": ["Aarav", "Diya", "Ishaan", "Meera", "Rohan"],
    "Math": [85, 92, 78, 88, 90],
    "Science": [82, 89, 84, 91, 87],
    "City": ["Dayton", "Columbus", "Cincinnati", "Dayton", "Columbus"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nSingle column:")
print(df["Name"])

print("\nMultiple columns:")
print(df[["Name", "Math"]])

print("\nMath >= 90:")
print(df[df["Math"] >= 90])

print("\nColumbus students with Science >= 85:")
print(df[(df["City"] == "Columbus") & (df["Science"] >= 85)])
