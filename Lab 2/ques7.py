import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("CarPrice_Assignment.csv")

print("First 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nStatistical Summary:")
print(df.describe())

df=df.drop_duplicates()
df.columns=df.columns.str.strip()

for col in df.select_dtypes(include='object').columns:
    df[col]=df[col].str.strip()

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())

plt.figure(figsize=(7,5))
sns.countplot(x='fueltype',data=df)
plt.title('Number of Cars by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Number of Cars')
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df['price'],bins=20)
plt.title('Distribution of Car Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x='enginesize',y='price',data=df)
plt.title('Engine Size vs Car Price')
plt.xlabel('Engine Size')
plt.ylabel('Price')
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df['price'])
plt.title('Boxplot of Car Prices')
plt.xlabel('Price')
plt.show()

plt.figure(figsize=(10,5))
plt.plot(df['car_ID'],df['price'])
plt.title('Car Price Trend')
plt.xlabel('Car ID')
plt.ylabel('Price')
plt.show()

plt.figure(figsize=(12,8))
corr=df.select_dtypes(include='number').corr()
sns.heatmap(corr,annot=True)
plt.title('Correlation Heatmap')
plt.show()

print("\nInsights:")
print("1. The dataset contains cars with different fuel types.")
print("2. Car prices vary significantly across the dataset.")
print("3. Engine size shows a relationship with car price.")
print("4. The boxplot helps identify possible outliers in car prices.")
print("5. The correlation heatmap shows relationships between numerical variables.")