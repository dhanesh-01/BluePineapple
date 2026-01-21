"""
10. Cohort Analysis (Intermediate)
    # Define cohort month = customer’s first order month.
    # For each cohort, compute:
    # number of active customers by month offset (M0, M1, M2…)
    # retention rate matrix (cohort table)
    # Output as a DataFrame shaped like a retention heatmap table (values as %).
"""
import pandas as pd

orders_df=pd.read_csv("./orders.csv")
orders_df['order_month']=pd.to_datetime(orders_df['order_date']).dt.to_period('M')

    # Define cohort month = customer’s first order month.
orders_df['first_order_month'] = (
    orders_df.groupby('customer_id')['order_month']
    .transform('min')
)

    # number of active customers by month offset (M0, M1, M2…)
orders_df["month_offset"] = (
    orders_df["order_month"] - orders_df["first_order_month"]
).apply(lambda x: x.n)

    # retention rate matrix (cohort table)
cohort_counts = (
    orders_df
    .groupby(["first_order_month", "month_offset"])["customer_id"]
    .nunique()
)
cohort_table = cohort_counts.unstack()
retention_table = cohort_table.divide(cohort_table[0], axis=0) * 100
retention_table = retention_table.round(2)
print(retention_table)

