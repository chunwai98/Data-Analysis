import pandas as pd
import matplotlib.pyplot as plt


# create dataframes
data={
    'Name':['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}

df=pd.DataFrame(data)
print('DataFrame:')
print(df)
print('Describe:')
print(df.describe())
print('Information:')
print(df.info())


filler_df=df[df['Age']>25]
print("The age > 25:")
print(filler_df)


plt.figure(figsize=(8,4))
plt.bar(df["Name"],df["Salary"])
plt.title("Example 1")
plt.xlabel("Name")
plt.ylabel("Salary")

plt.show()
