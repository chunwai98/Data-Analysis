import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyparsing import alphas

# Dataset with patient records
data = {
    'PatientID': [1001, 1002, 1003, 1001, 1004, 1005, 1002, 1006, 1003, 1007],
    'Age': [32, 45, 28, 32, 67, np.nan, 45, 59, 28, 71],
    'Gender': ['M', 'F', 'M', 'M', 'F', 'F', 'F', np.nan, 'M', 'F'],
    'BloodPressure': ['120/80', '140/90', np.nan, '120/80', '130/85', '115/75', '140/90', '150/95', '125/82', '160/100'],
    'Cholesterol': ['Normal', 'High', 'Normal', 'Normal', 'Borderline', 'Normal', 'High', np.nan, 'Normal', 'High'],
    'VisitDate': ['2023-01-15', '2023-02-20', '2023-03-10', '2023-01-15', '2023-04-05',
                  '2023-05-12', '2023-02-20', '2023-06-18', '2023-03-10', '2023-07-22']
}

df = pd.DataFrame(data)
print("=== Raw Patient Dataset ===")
print(df)
print("\nDF info:")
print(df.info())

# Data Cleaning
print("\n=== Data Cleaning ===")
df["VisitDate"]=pd.to_datetime(df["VisitDate"])
print("Duplicate Data?")
print(df.duplicated().values.any())
if df.duplicated().values.any():
    # Handle duplicates
    df=df.drop_duplicates(subset="PatientID")
    print("\nDF after remove Duplicate:")
    print(df)

# Fill missing values
df["Age"]=df["Age"].fillna(df.groupby("Gender")["Age"].transform("mean"))
df[["Gender","Cholesterol"]]=df[["Gender","Cholesterol"]].fillna("Unknown")

# Split blood pressure into two numeric columns
df[['Systolic', 'Diastolic']] = df['BloodPressure'].str.split('/', expand=True).replace(np.nan, 0).astype(int)

# Add Age Group
bins = [0, 30, 50, 70, 100]
labels = ['<30', '30-50', '50-70', '70+']
df["AgeGroup"]=pd.cut(df["Age"],bins=bins, labels=labels)

print("\nDataFrame after clean NaN value:")
print(df)

# Plot 1: Age Distribution
plt.figure(figsize=(10,4))
count_value=df["AgeGroup"].value_counts()
count_value.sort_index().plot(kind='bar', color='skyblue')
plt.title("Patient Age Distribution")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.grid(axis='y',alpha=0.2)
plt.tight_layout()


# Plot 2: Blood Pressure Analysis
plt.figure(figsize=(10,5))
plt.scatter(df['Systolic'], df['Diastolic'], c=pd.factorize(df['Cholesterol'])[0], cmap='viridis', alpha=1)
plt.colorbar(label='Cholesterol (0=Normal, 1=Borderline, 2=High)')
plt.title("Blood Pressure vs Cholesterol Levels")
plt.xlabel("Systolic Pressure")
plt.ylabel("Diastolic Pressure")
plt.grid(alpha=0.2)
plt.tight_layout()

#Plot 3: Patient visit frequency
plt.figure(figsize=(10,5))
gender_group=df["Gender"].value_counts()
gender_group.plot(kind="bar",color="yellow")
plt.title("Gender visit frequency")
plt.xlabel("Gender")
plt.xticks(rotation=0)
plt.ylabel("Count")

plt.show()