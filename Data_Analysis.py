# Description: Exploratory analysis of cleaned Telco Churn dataset

import pandas as pd

# Load cleaned dataset
INPUT_PATH = "data/cleaned_data.csv"
df = pd.read_csv(INPUT_PATH)

# Basic shape and info
print("\nDataset Shape:", df.shape)
print("\nColumn Summary:")
print(df.describe(include='all'))

# Churn distribution
print("\nChurn Rate:")
print(df['Churn_Yes'].value_counts(normalize=True) * 100)

# Correlation matrix
print("\nCorrelation Matrix:")
correlation_matrix = df.corr(numeric_only=True)
print(correlation_matrix['Churn_Yes'].sort_values(ascending=False))

# Grouped insights
contract_churn = df.groupby('Contract_Two year')['Churn_Yes'].mean()
payment_churn = df.groupby('PaymentMethod_Electronic check')['Churn_Yes'].mean()

print("\nChurn Rate by Contract Type (Two Year):")
print(contract_churn)

print("\nChurn Rate by Payment Method (Electronic Check):")
print(payment_churn)
