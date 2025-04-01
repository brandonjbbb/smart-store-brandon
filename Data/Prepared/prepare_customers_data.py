import pandas as pd
import os

RAW_DATA_PATH = '../../Data/Raw/customers_data.csv'
PREPARED_DATA_PATH = '../../Data/Prepared/customers_cleaned.csv'

# Load tab-separated data
df = pd.read_csv(RAW_DATA_PATH, sep='\t')
print(f"Original rows: {df.shape[0]}")
print("Columns:", df.columns.tolist())

# Clean: drop missing rows and duplicates
df.dropna(subset=['CustomerID', 'Name', 'Region', 'JoinDate'], inplace=True)
df.drop_duplicates(inplace=True)

# Save cleaned file
os.makedirs(os.path.dirname(PREPARED_DATA_PATH), exist_ok=True)
df.to_csv(PREPARED_DATA_PATH, index=False)
print(f"Cleaned rows: {df.shape[0]}")
