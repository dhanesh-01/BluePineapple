"""
7. Joins / Merges (Customers + Orders)
    # Create a customers DataFrame: customer_id , signup_date , segment .
    # Merge with orders.
    # Compute revenue by segment and retention proxy: “active in last 60 days” per segment.
"""
import pandas as pd

cust_df=pd.read_csv("./customers.csv")
order_df=pd.read_csv("./orders.csv")

# Outer merge on 'customer_id' column
merged_df = pd.merge(cust_df, order_df, on='customer_id', how='outer')
# print(merged_df)

# Compute revenue by segment and retention proxy: “active in last 60 days” per segment.
cols = ['signup_date', 'order_date']
merged_df[cols] = merged_df[cols].apply(pd.to_datetime, errors='coerce')

n=60  #last 60dyas
latest_order=merged_df['order_date'].max()
threshold = latest_order - pd.Timedelta(days=n)

print(merged_df[merged_df['order_date'] >threshold].groupby('segment').agg(
    revenue=('net_amount','sum'),
    active_last_60Days_customer=('customer_id','count')
))