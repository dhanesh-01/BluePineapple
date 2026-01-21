"""
# 6. Handling Missing Values
# Randomly introduce missing values in city, payment_mode, and discount_pct.
# Apply different strategies:
# fill categorical with “Unknown”
# fill numeric with median by category
# Prove it worked: show missing counts before/after.
"""
import pandas as pd
import numpy as np

df=pd.read_csv("./orders.csv")
for col in ["city", "payment_mode", "discount_pct"]:
    df.loc[df.sample(frac=0.1).index, col] = np.nan #fill the NaN 10% in data
df_deep_copy = df.copy(deep=True)

# fill categorical with "Unknown"
df["city"] = df["city"].fillna("Unknown")
df["payment_mode"] = df["payment_mode"].fillna("Unknown")
print("Fills the categorical with Unknown :\n",df)

# fill numeric with median by category
df['discount_pct'] = (
    df.groupby('category')['discount_pct']
    .transform(lambda x: x.fillna(x.median()))
)
print("After Filling NaN with Median :\n",df["discount_pct"])

# Prove it worked: show missing counts before/after.
print("\nmissing counts before : ",df_deep_copy.count())
print("\nmissing counts After : ",df.count())
