# Description: Data wrangling and cleaning script for Telco Churn dataset

import pandas as pd
import numpy as np
from scipy import stats

# Load the raw dataset
INPUT_PATH = "data/TelcoChurn.csv"
OUTPUT_PATH = "data/cleaned_data.csv"
df = pd.read_csv(INPUT_PATH)

# Drop duplicates if any
df.drop_duplicates(inplace=True)

# Convert 'TotalCharges' to numeric (some values may be missing or non-numeric)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Handling missing values
df.fillna({
    'Partner': df['Partner'].mode()[0],
    'DeviceProtection': df['DeviceProtection'].mode()[0],
    'TechSupport': df['TechSupport'].mode()[0],
    'MonthlyCharges': df['MonthlyCharges'].median(),
    'TotalCharges': df['TotalCharges'].median(),
}, inplace=True)

# Feature Engineering: convert SeniorCitizen from int to categorical
df['SeniorCitizen'] = df['SeniorCitizen'].map({1: 'Yes', 0: 'No'})

# Encoding categorical features using one-hot encoding (drop first to avoid dummy trap)
categorical_cols = df.select_dtypes(include='object').columns.tolist()
categorical_cols.remove('customerID')  # Exclude ID field
df_encoded = pd.get_dummies(df.drop(columns=['customerID']), columns=categorical_cols, drop_first=True)

# Outlier Detection and Removal using Z-score (only on numerical columns)
numeric_cols = df_encoded.select_dtypes(include=['int64', 'float64']).columns
z_scores = np.abs(stats.zscore(df_encoded[numeric_cols]))
df_encoded = df_encoded[(z_scores < 3).all(axis=1)]

# Save cleaned dataset
df_encoded.to_csv(OUTPUT_PATH, index=False)

print(f"Data cleaned and saved to {OUTPUT_PATH}. Shape: {df_encoded.shape}")
