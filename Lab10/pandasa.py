# Write a program to make Series and DataFrames using 
# pandas and perform basic operations.

import pandas as pd

marks = pd.Series([85, 90, 78, 92, 88])
print("Pandas Series:")
print(marks)

data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Age": [20, 21, 19, 20],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

print("\nFirst Two Rows:")
print(df.head(2))

print("\nDataFrame Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nStudent Names:")
print(df["Name"])

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nMaximum Marks:")
print(df["Marks"].max())

print("\nStudents with Marks > 80:")
print(df[df["Marks"] > 80])

print("\nSorted by Marks:")
print(df.sort_values(by="Marks", ascending=False))

df["Result"] = df["Marks"].apply(
    lambda mark: "Pass" if mark >= 40 else "Fail"
)

print("\nDataFrame with Result:")
print(df)

print("\nStatistical Summary:")
print(df["Marks"].describe())

