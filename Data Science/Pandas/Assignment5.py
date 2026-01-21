"""
# 5. Pivot Table Dashboard View
# Create a pivot:
# index: month (from order_date )
# columns: category
# values: net_amount sum
# Add a “Grand Total” column and compute month-over-month growth %.
"""
import pandas as pd

df=pd.read_csv("./orders.csv")
df["order_date"] = pd.to_datetime(df["order_date"])
df['month'] = df["order_date"].dt.to_period("M")

pivoted_df = pd.pivot_table(
    df,
    index="month",
    columns="category",
    values="net_amount",
    aggfunc="sum",
    fill_value=0
)

pivoted_df["Grand Total"] = pivoted_df.sum(axis=1)
pivoted_df["MoM Growth %"] = pivoted_df["Grand Total"].pct_change() * 100
print(pivoted_df)
