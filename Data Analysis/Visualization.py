# Description: Data visualization script for Telco Churn analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

sns.set(style="whitegrid")

# Load cleaned dataset
INPUT_PATH = "data/cleaned_data.csv"
df = pd.read_csv(INPUT_PATH)

# Plot churn distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='Churn_Yes', data=df, palette='pastel')
plt.title('Churn Distribution')
plt.xlabel('Churn (1=Yes, 0=No)')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("charts/churn_distribution.png")

# Monthly charges vs churn
plt.figure(figsize=(8, 5))
sns.boxplot(x='Churn_Yes', y='MonthlyCharges', data=df, palette='Set2')
plt.title('Monthly Charges by Churn')
plt.xlabel('Churn')
plt.ylabel('Monthly Charges')
plt.tight_layout()
plt.savefig("charts/monthly_charges_boxplot.png")

# Correlation heatmap
plt.figure(figsize=(12, 10))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=False, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig("charts/correlation_heatmap.png")

# Interactive: Churn vs Tenure using Plotly
fig = px.histogram(df, x="tenure", color="Churn_Yes",
                   title="Tenure vs Churn", nbins=30, barmode='overlay')
fig.write_html("charts/tenure_churn_plotly.html")

print("Visualizations saved to 'charts/' folder.")
