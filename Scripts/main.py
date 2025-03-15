import pandas as pd

# Sample data
data = {
    "CustomerID": [101, 102, 103, 101, 102, 104],
    "SaleAmount": [250.50, 130.75, 200.00, 300.25, 400.00, 150.00]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Total Revenue per Customer
customer_revenue = df.groupby("CustomerID")["SaleAmount"].sum().reset_index()
customer_revenue.rename(columns={"SaleAmount": "TotalRevenue"}, inplace=True)

# Print the result
print("Total Revenue per Customer:\n", customer_revenue)

# Save the result
customer_revenue.to_csv("../data/customer_total_revenue.csv", index=False)
