# Step 1: Import required libraries
import pandas as pd
import numpy as np

# Step 2: Generate sample dataset (simulating AI-assisted dataset generation)
data = {
    "Name": ["Alice", "Bob", "Charlie", "Alice", None, "Eve"],
    "Age": [25, 30, 35, 25, 28, None],
    "Email": ["alice@example.com", "bob@example.com", "charlie@example.com", "alice@example.com", "dave@example.com", None],
    "Country": ["USA", "USA", "UK", "USA", None, "India"]
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original Dataset:")
print(df)

# Step 3: Standardize column names (lowercase, replace spaces with underscores)
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Step 4: Handle missing values (NaN)
# Here we can fill missing values or drop rows/columns as needed
df['name'].fillna('Unknown', inplace=True)
df['age'].fillna(df['age'].median(), inplace=True)
df['email'].fillna('no_email@example.com', inplace=True)
df['country'].fillna('Unknown', inplace=True)

# Step 5: Remove duplicates
df.drop_duplicates(inplace=True)

# Step 6: Save cleaned data to CSV
df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned Dataset:")
print(df)

# Step 7: Demonstrate loading the cleaned CSV
loaded_df = pd.read_csv("cleaned_dataset.csv")
print("\nLoaded CSV to verify:")
print(loaded_df)
