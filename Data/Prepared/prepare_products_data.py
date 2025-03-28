import pandas as pd
import os

RAW_DATA_PATH = '../../Data/Raw/Products_Data.csv'
PREPARED_DATA_PATH = '../../Data/Prepared/products_cleaned.csv'

df = pd.read_csv(RAW_DATA_PATH, sep='\t')
print(f"Original rows: {df.shape[0]}")
print("Columns:", df.columns.tolist())

df.dropna(subset=['ProductID', 'ProductName', 'UnitPrice'], inplace=True)
df.drop_duplicates(inplace=True)

if 'UnitPrice' in df.columns:
    df = df[df['UnitPrice'] < df['UnitPrice'].quantile(0.95)]

os.makedirs(os.path.dirname(PREPARED_DATA_PATH), exist_ok=True)
df.to_csv(PREPARED_DATA_PATH, index=False)
print(f"Cleaned rows: {df.shape[0]}")
