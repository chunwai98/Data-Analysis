import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dataset with store information
data = {
    'StoreID': [101, 102, 103, 101, 104, 105, 102, 106, 103, 107],
    'Location': ['Urban', 'Suburban', 'Urban', 'Urban', 'Rural', 'Urban',
                 'Suburban', np.nan, 'Urban', 'Rural'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Electronics',
                 'Home', 'Clothing', 'Clothing', 'Home', np.nan, 'Home'],
    'Sales': [45000, 32000, 38000, 45000, 28000, np.nan, 32000, 41000, 38000, 29000],
    'Customers': [1200, 950, 1100, 1200, 700, 800, 950, np.nan, 1100, 750],
    'Month': ['Jan', 'Feb', 'Mar', 'Jan', 'Apr', 'May', 'Feb', 'Jun', 'Mar', 'Jul']
}
df = pd.DataFrame(data)

print("=== Raw Dataset ===")
print(df)
print("DataFrame Info:")
print(df.info())

# Data Cleaning
print("\n=== Data Cleaning ===")
print("Duplicate Data?")
print(df.duplicated().values.any())
if df.duplicated().values.any():
    # Remove duplicates keeping first occurrence
    df.drop_duplicates(subset=["StoreID"],inplace=True)
    print("\nDataFrame After drop Duplicate:")
    print(df)

df["Location"]=df["Location"].fillna("Unknown")
#Probably meant to standardize "Electronics" spelling:
df['Category'] = df['Category'].str.title().replace('Electronics', 'Electronics')
df["Sales"]=df["Sales"].fillna(df["Sales"].mean())
df["Customers"]=df["Customers"].fillna(df["Customers"].mean())
print("\nDataFrame after clean NaN value:")
print(df)

# Visualization 1: Sales by Location
location_df=df.groupby("Location")
sum_of_sales=location_df["Sales"].sum()
plt.figure(figsize=(10,5))
sum_of_sales.plot(kind="barh",color="teal")
plt.title("Total Sales by Store Location")
plt.xlabel("Amount")
plt.grid(True)

# Visualization 2: Monthly Customer Trends
month_df = df.groupby("Month")
mean_of_customers=month_df["Customers"].mean()
plt.figure(figsize=(10,5))
mean_of_customers.plot(kind='line', marker='x',color='purple')
plt.title('Average Customers per Month')
plt.ylabel('Number of Customers')
plt.grid(True)

plt.show()