# unemployment_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv("Unemployment in India.csv")

# Step 2: Preview the dataset
print("Dataset Preview:")
print(df.head())

# Step 3: Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Clean column names if needed
df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()

# Step 5: Convert date column to datetime format (if exists)
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])

# Step 6: Data summary
print("\nData Summary:")
print(df.describe(include='all'))

# Step 7: Visualize unemployment rate by region
plt.figure(figsize=(12, 6))
sns.barplot(x='region', y='estimated_unemployment_rate_(%)', data=df, ci=None)
plt.xticks(rotation=90)
plt.title('Unemployment Rate by Region')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.tight_layout()
plt.show()

# Step 8: Time series plot of unemployment over time
if 'date' in df.columns:
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='date', y='estimated_unemployment_rate_(%)', hue='region', data=df)
    plt.title('Unemployment Rate Over Time by Region')
    plt.ylabel('Estimated Unemployment Rate (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Step 9: Average unemployment by region
region_avg = df.groupby('region')['estimated_unemployment_rate_(%)'].mean().sort_values(ascending=False)
print("\nAverage Unemployment Rate by Region:")
print(region_avg)
