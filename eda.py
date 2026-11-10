import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books_data.csv")

print(df.head())

# Dataset overview
print("\n--- DATASET INFORMATION ---")
df.info()

# Number of rows and columns
print("\n--- DATASET SHAPE ---")
print(df.shape)

# Column names
print("\n--- COLUMN NAMES ---")
print(df.columns)

# Check missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# Check duplicate records
print("\n--- DUPLICATE RECORDS ---")
print("Total duplicate rows:", df.duplicated().sum())

# Count unique values in each column
print("\n--- UNIQUE VALUES ---")
print(df.nunique())

# Price statistics
print("\n--- PRICE STATISTICS ---")
print(df["Price"].describe())

# Most expensive book
print("\n--- MOST EXPENSIVE BOOK ---")
print(df.loc[df["Price"].idxmax(), ["Title", "Price"]])

# Cheapest book
print("\n--- CHEAPEST BOOK ---")
print(df.loc[df["Price"].idxmin(), ["Title", "Price"]])

# Book rating distribution
print("\n--- BOOK RATING DISTRIBUTION ---")
print(df["Rating"].value_counts())

# Average price by rating
print("\n--- AVERAGE PRICE BY RATING ---")
print(df.groupby("Rating")["Price"].mean().sort_values(ascending=False))

# Book availability
print("\n--- BOOK AVAILABILITY ---")
print(df["Availability"].value_counts())

# Outlier detection using IQR
print("\n--- OUTLIER DETECTION ---")
Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)
outliers = df[(df["Price"] < lower_limit) | (df["Price"] > upper_limit)]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower limit:", lower_limit)
print("Upper limit:", upper_limit)
print("Number of outliers:", len(outliers))
print(outliers[["Title", "Price"]])

# Price distribution histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=10, edgecolor="black")
plt.title("Distribution of Book Prices")
plt.xlabel("Book Price (£)")
plt.ylabel("Number of Books")
plt.show()
