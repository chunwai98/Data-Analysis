import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

df=pd.read_excel("Simple Sales Data (Toy Store).xlsx", sheet_name="Sheet1")

print("=== Raw Patient Dataset ===")
print(df)
print("\nDF info:")
print(df.info())


print("\n=== Data Cleaning ===")
# remove Duplicate
print(df.duplicated())
if df.duplicated().values.any():
    df=df.drop_duplicates()
    print("\nDataFrame after Drop Duplicate :")
    print(df)

#fill NaN
# df["Units_Sold"]=df["Units_Sold"].fillna(df.groupby("Product")["Units_Sold"].mean())
df["Units_Sold"]=df["Units_Sold"].fillna(df.groupby("Product")["Units_Sold"].transform("mean"))
df["Unit_Price"]=df["Unit_Price"].fillna(df["Unit_Price"].median())
df["Revenue"]=df["Revenue"].fillna(df["Units_Sold"]*df["Unit_Price"])

print("\nDataFrame after clean NaN value:")
print(df)

#Plot Revenue per Product
plt.figure(figsize=(10,5))
product_group=df.groupby("Product")
total_revenue=product_group["Revenue"].sum()
total_revenue.plot(kind="bar",color="skyblue")
plt.ylabel("Total Revenue")
plt.xlabel("Product")
plt.xticks(rotation=0)
plt.title("Revenue per Product")


plt.show()


