# customer-retention

# :clipboard: Project Overview
Many companies struggle with customer retention. This project uses an online dataset to check the cause of retention and to improve the project using Project Management tools and techniques. Data analysis will be used to find the cause and trends.

# :clipboard: Objectives

## Analytics Side:

* Analyze customer churn (who is leaving and why)

* Identify trends, high-risk customer segments, and major reasons for churn

* Develop predictive models (optional but recommended) to forecast churn

## Project Management Side:

* Create a Project Charter

* Build a Work Breakdown Structure (WBS)

* Develop a timeline using Gantt charts or Kanban

* Identify stakeholders and risks

* Propose action items based on data insights

# :clipboard: Dataset
* The Telco Customer Churn Dataset is used in this project. This dataset is open to use on Kaggle, which contains some customer demographics, services signed up for, account information, and whether the customer churned or not.
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

# :bookmark: Step by Step Plan
1. Project Management Foundation
   * Project Charter
   * WBS and Gantt Chart
   * Risk Assessment
   * KPIs
  
2. Data Wrangling & EDA
   * Clean the dataset
   * Perform exploratory data analysis (EDA)
   * Correlation analysis and hypothesis testing

3. Reporting & Recommendations
   * Create a dashboard
   * Prepare final report
   * Suggest strategies
  
# :bookmark: Pipeline Components

## Data_Cleaning.py – Data Wrangling and Preprocessing
* Loaded the raw Telco dataset.
* Handled missing values using mean, median, and mode-based imputation.
* Converted inconsistent datatypes (e.g., TotalCharges to numeric).
* Applied one-hot encoding to categorical variables.
* Removed outliers using Z-score filtering.
* Saved a cleaned dataset to data/cleaned_data.csv.

## Data_Analysis.py – Exploratory Data Analysis (EDA)
* Computed summary statistics and correlation metrics.
* Analyzed churn distribution and correlations with features like:
  1. Monthly charges
  2. Contract type
  3. Payment method
* Grouped data to assess churn rate trends across segments (e.g., Contract_Two year, PaymentMethod_Electronic check).

## Visualization.py – Data Visualization
* Created multiple visual outputs:
  1. Churn Distribution: Count of churned vs. retained customers.
  2. Boxplot of Monthly Charges vs. Churn: Churn is higher with higher charges.
  3. Correlation Heatmap: MonthlyCharges, Contract type, and OnlineSecurity show strong relationships with churn.
  4. Tenure vs. Churn: An interactive Plotly chart shows churn decreases with customer tenure.
* Visuals were saved in the charts/ directory, including an interactive tenure_churn_plotly.html.

## Main.py – Automation Script
* Runs the above steps in sequence.
* Ensures necessary directories (data/, charts/) are created.
* Useful for quick reruns or integrations into a larger project pipeline.

# :bookmark: Key Findings from the Analysis
1. Contract Type Matters: Customers on month-to-month contracts churn the most. Two-year contracts drastically reduce churn rates.

2. Electronic Check Payment Method is Risky: Customers who pay via electronic checks have significantly higher churn rates, suggesting dissatisfaction or lack of commitment.

3. High Monthly Charges Correlate with Churn: The higher the monthly fee, the more likely a customer is to churn, especially without bundled value services.

4. Customer Tenure is Crucial: Newer customers (low tenure) are more likely to leave. Churn decreases significantly with time.

5. Security and Support Services Reduce Churn: Availability of online security, device protection, and tech support correlates with lower churn rates.

# :bookmark: Recommendations for Customer Retention

* Incentivize Long-Term Contracts: Offer discounts or perks for 1–2 year subscriptions.
* Bundle Support Services: Provide online security and tech support at a discount for newer customers.
* Follow-Up on High-Paying Customers: Offer loyalty benefits or periodic check-ins to those paying higher monthly rates.
* Improve Onboarding and Early Engagement: Implement welcome campaigns and dedicated onboarding for new clients (<6 months).
* Rethink Electronic Check Payments: Push for auto-pay credit card or digital wallet options with benefits.


