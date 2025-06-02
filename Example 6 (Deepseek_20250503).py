import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

df=pd.read_excel("Deepseek_20250503.xlsx", sheet_name="deepseek_20250503")

print("=== Raw Patient Dataset ===")
print("\nDataFrame Info:")
print(df.info())
print(df)

print("\n=== Data Cleaning ===")
print("\nAny Duplicate Rows?")
print(df.duplicated().values.any())
if df.duplicated().values.any():
    print("Cleaning Duplicate Rows...")
    df=df.drop_duplicates()

print("\nAny NaN Rows?")
print(df.isna().values.any())
df["Sales"]=df["Sales"].fillna(df.groupby("Product")["Sales"].transform("mean"))
df["Profit"]=df["Profit"].fillna(df["Sales"]-df["Expenses"])

if not df.isna().values.any():
    print("\nDataFrame after clean NaN value:")
    print(df)
else:
    print("\nDataFrame NaN value:")
    print(df.isna())

# visualizations
#Monthly sales trends for each product
plt.figure(figsize=(12,6))
monthly=df.groupby("Month")
total_sales=monthly["Sales"].sum()
total_sales.plot(kind="bar",color="#ADD8E6")
plt.grid(axis="y",alpha=0.2)
plt.title("Monthly sales trends for each product")
plt.ylabel("Total Sales")
plt.xlabel("Month")
plt.xticks(rotation=0)

#Profit comparison between products
plt.figure(figsize=(12,6))
products=df.groupby("Product")
total_profit=products["Profit"].sum()
total_profit.plot(kind='bar',color="yellow")
plt.ylabel("Total Profits")
plt.xlabel("Products")
plt.xticks(rotation=0)

#Expenses vs Sales scatter plot
plt.figure(figsize=(10,6))
plt.scatter(df['Sales'],df['Expenses'], alpha=0.6, edgecolors='w')
plt.title('Sales vs Profit Correlation')
plt.xlabel('Sales')
plt.ylabel('Expenses')
plt.grid(alpha=0.2)


plt.show()