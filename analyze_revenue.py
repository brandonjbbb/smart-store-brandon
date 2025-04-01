import pandas as pd

# Load the data from CSV
df = pd.read_csv("sales_data.csv")

# Ensure data is clean
df.dropna(subset=['CustomerID', 'SaleAmount'], inplace=True)
df['SaleAmount'] = pd.to_numeric(df['SaleAmount'], errors='coerce')

# Group by CustomerID and sum SaleAmount
customer_revenue = df.groupby('CustomerID')['SaleAmount'].sum().reset_index()
customer_revenue.rename(columns={'SaleAmount': 'TotalRevenue'}, inplace=True)

# Sort customers by Total Revenue (highest first)
customer_revenue = customer_revenue.sort_values(by='TotalRevenue', ascending=False)

# Display results
print(customer_revenue)

# Save the output to a new CSV file
customer_revenue.to_csv("customer_total_revenue.csv", index=False)
