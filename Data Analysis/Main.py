# Description: Runs the complete Telco Churn project pipeline

import subprocess
import os

# Ensure necessary directories exist
os.makedirs("charts", exist_ok=True)
os.makedirs("data", exist_ok=True)

print("--- Running Data Cleaning ---")
subprocess.run(["python3", "Data_Cleaning.py"])

print("\n--- Running Data Analysis ---")
subprocess.run(["python3", "Data_Analysis.py"])

print("\n--- Generating Visualizations ---")
subprocess.run(["python3", "Visualization.py"])

print("\nAll steps completed. Check 'charts/' for visualizations and 'data/' for cleaned dataset.")
