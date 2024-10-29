import pandas as pd


# # import the data from both tabs in the "Bank_Churn_Messy" Excel file
account_info = pd.read_excel('Bank_Churn_Messy.xlsx', sheet_name='Account_Info')
customer_info = pd.read_excel('Bank_Churn_Messy.xlsx', sheet_name='Customer_Info')


# Perform left join
merged_df = account_info.merge(customer_info, how='left', on='CustomerId')

# remove the duplicate on the merged dataframe
# merged_df_no_duplicates = merged_df.drop_duplicates()

# Check the shape of the resulting dataframe
print(f"Shape of merged dataframe: {merged_df.shape}")

# Preview the first few rows
print(merged_df.head()) 