"""
9. Outlier Detection + Capping (Intermediate)
For each category:
compute IQR of net_amount
flag outliers (outside [Q1-1.5IQR, Q3+1.5IQR])
cap outliers to bounds (winsorize)
Report outlier counts by category before/after.

"""
import pandas as pd
import numpy as np
orders_df=pd.read_csv("./orders.csv")

stats=orders_df.groupby('category')['net_amount'].agg(
    Q1=lambda x:x.quantile(0.25),
    Q3=lambda x:x.quantile(0.75),
)

stats['IQR']=stats['Q3']-stats['Q1']

# Lower bound = Q1 - 1.5 × IQR & Upper bound = Q3 + 1.5 × IQR   to replace outliers
stats['lower']=stats['Q1']-1.5*stats['IQR']
stats['upper']=stats['Q3']+1.5*stats['IQR']

orders_df = orders_df.merge(
    stats[["lower", "upper"]],
    on="category",
    how="left"
)

#Flag outliers BEFORE
orders_df["is_outlier_before"] = (
    (orders_df["net_amount"] < orders_df["lower"]) |
    (orders_df["net_amount"] > orders_df["upper"])
)
outlier_count_before = (orders_df.groupby("category")["is_outlier_before"].sum())
print("\nOutliers before cap:\n", outlier_count_before)

# Cap (winsorize)
orders_df["net_amount"] = orders_df["net_amount"].clip(
    lower=orders_df["lower"],
    upper=orders_df["upper"]
)


#Flag outliers AFTER
orders_df["is_outlier_after"] = (
    (orders_df["net_amount"] < orders_df["lower"]) |
    (orders_df["net_amount"] > orders_df["upper"])
)
outlier_count_after = (orders_df.groupby("category")["is_outlier_after"].sum())
print("\nOutliers after cap:\n", outlier_count_after)
