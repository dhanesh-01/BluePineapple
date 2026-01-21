"""
8. Window Functions (Intermediate)
    # For each customer:
    # sort by order_date
    # compute prev_order_date
    # compute days_since_prev
    # compute rolling 3-order average net_amount
    # Identify customers whose average order value is increasing (simpleheuristic).
"""
import pandas as pd
customers_df=pd.read_csv("./customers.csv")
orders_df=pd.read_csv("./orders.csv")

    # sort by order_date
orders_df['order_date']=pd.to_datetime(orders_df['order_date'])
orders_df=orders_df.sort_values(by='order_date')
print(orders_df)

    # compute prev_order_date
orders_df['prev_order_date']=orders_df.groupby('customer_id')['order_date'].shift(1)
print(orders_df)

    # compute days_since_prev
orders_df['days_since_prev']=(orders_df['order_date']-orders_df['prev_order_date']).dt.days
print(orders_df)

    # compute rolling 3-order average net_amount
orders_df["rolling_3_avg"] = (
    orders_df.groupby("customer_id")["net_amount"]
      .rolling(window=3, min_periods=1)
      .mean()
      .reset_index(level=0, drop=True)
)
print(orders_df)

    # Identify customers whose average order value is increasing (simpleheuristic).
orders_df["is_increasing"] = (
    orders_df.groupby("customer_id")["rolling_3_avg"]
    .transform("last") >
    orders_df.groupby("customer_id")["rolling_3_avg"]
    .transform("first")
)
print("customers whose average order value is increasing\n ",orders_df)