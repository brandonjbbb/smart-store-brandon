import pandas as pd
import os

RAW_DATA_PATH = '../../Data/Raw/customers_data.csv'
PREPARED_DATA_PATH = '../../Data/Prepared/customers_cleaned.csv'

df = pd.read_csv(RAW_DATA_PATH, sep='\t')
print(f"Original rows: {df.shape[0]}")
print("Fixed Columns:", df.columns.tolist())

df.dropna(subset=['CustomerID', 'Name', 'Region', 'JoinDate'], inplace=True)
df.drop_duplicates(inplace=True)

os.makedirs(os.path.dirname(PREPARED_DATA_PATH), exist_ok=True)
df.to_csv(PREPARED_DATA_PATH, index=False)
print(f"Cleaned rows: {df.shape[0]}")
