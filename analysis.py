import numpy as np
import pandas as pd

np.random.seed(42)
dates = pd.date_range(start="2025-01-01", end="2025-12-31", freq="D")
data = {
    "Order_ID": [f"ORD-{i}" for i in range(1000)],
    "Order_Date": np.random.choice(dates, 1000),
    "Region": np.random.choice(
        ["North", "South", "East", "West", "Central"], 1000
    ),
    "Category": np.random.choice(
        ["Electronics", "Furniture", "Clothing", "Office Supplies"], 1000
    ),
    "Product": np.random.choice(
        ["Laptop", "Desk", "Shirt", "Pen", "Monitor", "Chair"], 1000
    ),
    "Quantity": np.random.randint(1, 5, 1000),
    "Unit_Price": np.random.uniform(10, 500, 1000),
}
df = pd.DataFrame(data)
df["Total_Revenue"] = df["Quantity"] * df["Unit_Price"]
print(df.head())
# 2. KEY PERFORMANCE INDICATORS (KPIs)
total_revenue = df["Total_Revenue"].sum()
total_units = df["Quantity"].sum()
total_orders = df["Order_ID"].nunique()
avg_order_value = total_revenue / total_orders

print("\n--- Overall Business KPIs ---")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Units Sold: {total_units:,}")
print(f"Total Orders: {total_orders:,}")
print(f"Average Order Value: ${avg_order_value:,.2f}")

# 3. TOP-SELLING PRODUCTS
top_products = (
    df.groupby("Product")["Total_Revenue"]
    .sum()
    .reset_index()
    .sort_values(by="Total_Revenue", ascending=False)
)
print("\n--- Top-Selling Products by Revenue ---")
print(top_products.head(3))

# 4. REGIONAL PERFORMANCE
regional_performance = (
    df.groupby("Region")["Total_Revenue"]
    .sum()
    .reset_index()
    .sort_values(by="Total_Revenue", ascending=False)
)
print("\n--- Regional Performance ---")
print(regional_performance)
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid")

# Figure: Regional Performance Bar Chart
plt.figure(figsize=(8, 4))
sns.barplot(
    x="Region", y="Total_Revenue", data=regional_performance, palette="viridis"
)
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Total Revenue ($)")
plt.tight_layout()
plt.savefig("regional_performance.png")
plt.close()
print("\nChart saved successfully as regional_performance.png!")