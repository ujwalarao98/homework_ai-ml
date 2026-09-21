import pandas as pd
import numpy as np

data = {
    "Name": ["Aarav", "Diya", "Ishaan", "Meera", "Rohan"],
    "Math": [85, np.nan, 78, 88, np.nan],
    "Science": [82, 89, np.nan, 91, 87]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nMissing values:")
print(df.isnull())

print("\nMissing-value count:")
print(df.isnull().sum())

filled_df = df.copy()
filled_df["Math"] = filled_df["Math"].fillna(filled_df["Math"].mean())
filled_df["Science"] = filled_df["Science"].fillna(filled_df["Science"].mean())

print("\nAfter filling missing values:")
print(filled_df)

print("\nAfter dropping rows with missing values:")
print(df.dropna())
