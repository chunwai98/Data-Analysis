import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Product': ['A', 'B', 'A', 'C', 'B', 'D', 'A', np.nan, 'C', 'B'],
    'Sales': [150, 200, 150, 350, 200, 400, np.nan, 300, 350, 200],
    'Month': ['Jan', 'Feb', 'Jan', 'Mar', 'Feb', 'Apr', 'Jan', 'May', 'Mar', 'Feb'],
    'Region': ['North', 'South', 'North', np.nan, 'South', 'East', 'North', 'West', np.nan, 'South']
}

df=pd.DataFrame(data)
print("DataFrame:")
print(df)
#verify duplicate and nan rows in dataframe
print("DataFrame Info:")
print(df.info())
#find the duplicate rows
print("duplicate value?")
print(df.duplicated())
#drop the duplicates rows
new_df=df.drop_duplicates()
print(new_df)
#drop the duplicate rows base on column
new_df=new_df.dropna(subset=["Region","Product"])
print(new_df)
print("is NaN value in Dataframe?")
print(new_df.isna())
new_df["Sales"]=new_df["Sales"].fillna(200)
print(new_df)

month_df=new_df.groupby("Month")
print("Sum of Sales of Month:")
sum_sales=month_df["Sales"].sum()
print(sum_sales)
plt.figure(figsize=(10,5))
sum_sales.plot(kind="bar",color="skyblue")
plt.title('Total Sales by Month')
plt.ylabel('Sales Amount')


product_df=new_df.groupby("Product")
sum_product=product_df["Sales"].sum()
print("Sum of sales of Product:")
print(sum_product)
plt.figure(figsize=(10,5))
sum_product.plot(kind="bar", color="red")
plt.title("Total Sales by Product")
plt.ylabel("Sales Amount")



plt.show()