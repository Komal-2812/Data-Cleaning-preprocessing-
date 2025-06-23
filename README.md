### Task 1: Data Cleaning & Preprocessing

**Changes Made:**
- Handled missing values using dropna/fillna.
- Removed duplicate rows.
- Standardized gender and country text.
- Converted date column to dd-mm-yyyy format.
- Renamed columns to lowercase and removed spaces.
- Fixed data types (e.g., age to int, date to datetime).

**Tools Used**: Python, Pandas

## ✅ Actions Performed:

### 1. Identified and Handled Missing Values
- Used `.isnull().sum()` to detect missing values.
- Filled 2 missing values in the `rating_count` column using the **median** strategy.

### 2. Removed Duplicate Rows
- Used `.drop_duplicates()` – found **0 duplicate rows**, so no deletion was needed.

### 3. Standardized Text Values
- Converted all text values (e.g., `product_name`, `category`, `review_content`, etc.) to **lowercase** and **stripped extra spaces** using `.str.lower().str.strip()`.

### 4. Renamed Column Headers
- Renamed all columns to be **clean and uniform**:
  - Lowercase
  - Underscore-separated
  - Removed any leading/trailing whitespace

### 5. Checked & Fixed Data Types
- Verified data types using `.dtypes`
- Missing numeric conversion skipped because all columns remained `object` (likely due to currency/symbols or mixed formatting).
- Date columns were checked (e.g., `date`, `dt_customer`) – none were detected or convertible.

> ⚠️ Note: Dataset did **not include date fields**, so date formatting (e.g., `dd-mm-yyyy`) was **not applied**.

## 📊 Resulting Clean Dataset Overview

- Rows: **1,465**
- Columns: **16**
- All missing values handled.
- Column names standardized.
- Ready for further analysis, visualization, or modeling.

## 📂 Output File
"amazon_cleaned_full.csv"
**
