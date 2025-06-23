import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("amazon.csv")
print("🔹 Original Dataset:\n", df.head())
print("Shape:", df.shape)
print("\n")

# Step 2: Check missing values
print("🔹 Missing Values (Before Cleaning):\n", df.isnull().sum())
print("\n")

# Step 3: Remove commas and spaces from numeric fields
for col in ['discounted_price', 'actual_price', 'rating', 'rating_count']:
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace(',', '').str.strip()

# Step 4: Convert to numeric
for col in ['discounted_price', 'actual_price', 'rating', 'rating_count']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

print("🔹 After Converting to Numeric:\n", df[['discounted_price', 'actual_price', 'rating', 'rating_count']].dtypes)
print("\n")

# Step 5: Handle missing values (e.g., rating_count)
if 'rating_count' in df.columns:
    median_val = df['rating_count'].median()
    df['rating_count'].fillna(median_val, inplace=True)
    print(f"🔹 Filled missing 'rating_count' with median: {median_val}")
    print("Missing Values After Filling:\n", df[['rating_count']].isnull().sum())
print("\n")

# Step 6: Drop duplicate rows
duplicates_before = df.duplicated().sum()
df.drop_duplicates(inplace=True)
print(f"🔹 Duplicates Removed: {duplicates_before}")
print("New Shape after removing duplicates:", df.shape)
print("\n")

# Step 7: Standardize text values (example: category)
if 'category' in df.columns:
    df['category'] = df['category'].str.strip().str.lower()
    print("🔹 Standardized 'category' values:\n", df['category'].unique())
print("\n")

# Step 8: Rename columns
print("🔹 Column Names Before Renaming:\n", df.columns.tolist())
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_').str.replace('-', '_')
print("🔹 Column Names After Renaming:\n", df.columns.tolist())
print("\n")

# Step 9: Convert date columns if any
date_cols = []
for col in df.columns:
    if 'date' in col:
        df[col] = pd.to_datetime(df[col], errors='coerce')
        date_cols.append(col)
if date_cols:
    print("🔹 Converted to datetime:", date_cols)
else:
    print("🔹 No date columns found to convert.")
print("\n")

# Step 10: Save cleaned dataset
df.to_csv("amazon_cleaned_full.csv", index=False)
print("✅ Cleaned dataset saved as 'amazon_cleaned_full.csv'")
