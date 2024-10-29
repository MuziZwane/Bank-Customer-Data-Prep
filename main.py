import pandas as pd

 # import the data from both tabs in the "Bank_Churn_Messy" Excel file
account_info = pd.read_excel('Bank_Churn_Messy.xlsx', sheet_name='Account_Info')
customer_info = pd.read_excel('Bank_Churn_Messy.xlsx', sheet_name='Customer_Info')


# Remove duplicate rows
account_info = account_info.drop_duplicates()
customer_info = customer_info.drop_duplicates()

# Remove duplicate columns
account_info = account_info.T.drop_duplicates().T
customer_info = customer_info.T.drop_duplicates().T

# Perform left join on the correct column names
merged_df = account_info.merge(customer_info, how='left', on='CustomerId')

# Rename tenure_x to tenure and drop tenure_y
if 'Tenure_x' in merged_df.columns:
    merged_df = merged_df.rename(columns={'Tenure_x': 'Tenure'})
    merged_df = merged_df.drop('Tenure_y', axis=1, errors='ignore')


# Check the result
print(merged_df.head())