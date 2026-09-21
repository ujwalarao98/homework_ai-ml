import pandas as pd
from pathlib import Path

file_path = Path(__file__).with_name("students.csv")
df = pd.read_csv(file_path)

print("Complete DataFrame:")
print(df)

print("\nHEAD:")
print(df.head())

print("\nTAIL:")
print(df.tail())

print("\nINFO:")
df.info()

print("\nDESCRIBE:")
print(df.describe())

print("\nShape:", df.shape)
print("Columns:", list(df.columns))
