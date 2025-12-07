import pandas as pd

# Load dataset using absolute path
df = pd.read_csv(r"C:\Users\adria\Documents\dataset.csv.csv")

# Display first 5 rows
print("\n=== FIRST 5 ROWS ===")
print(df.head())

# DataFrame info
print("\n=== DATAFRAME INFO ===")
print(df.info())

# Descriptive statistics
print("\n=== DESCRIPTIVE STATISTICS ===")
print(df.describe())

# Access rows and columns
print("\n=== loc: SINGLE ROW BY LABEL (index 0) ===")
print(df.loc[0])

print("\n=== iloc: SINGLE ROW BY POSITION (row 1) ===")
print(df.iloc[1])

print("\n=== loc: SLICE BY LABEL (rows 0 to 2) ===")
print(df.loc[0:2])

print("\n=== iloc: SLICE BY POSITION (rows 1 to 3) ===")
print(df.iloc[1:4])

print("\n=== SINGLE COLUMN (Salary) ===")
print(df["Salary"])

print("\n=== SINGLE CELL (row 2, column 'Age') ===")
print(df.loc[2, "Age"])

# Boolean filters
print("\n=== FILTER: Age > 30 ===")
print(df[df["Age"] > 30].head())

print("\n=== FILTER: (Age > 25) & (Department == 'IT') ===")
print(df[(df["Age"] > 25) & (df["Department"] == "IT")].head())

# Add new column
df["Salary_Double"] = df["Salary"] * 2
print("\n=== ADDED COLUMN Salary_Double ===")
print(df.head())

# Drop the column
df = df.drop("Salary_Double", axis=1)
print("\n=== COLUMNS AFTER DROP ===")
print(df.columns)

# Groupby example
print("\n=== AVERAGE SALARY BY DEPARTMENT ===")
print(df.groupby("Department")["Salary"].mean())

print("\n=== SCRIPT COMPLETE ===")
