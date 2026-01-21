"""
# 3. Filtering + Multi-condition Queries
# Filter orders:
# category in a set (e.g., Electronics/Fashion)
# net_amount > X
# order_date within last N days (relative to max date )
# Output count + total net_amount .
"""
import pandas as pd

df=pd.read_csv("./orders.csv")

# category in a set (e.g., Electronics/Fashion)
category_set =("Electronics","Fashion")
condition1= df['category'].isin(category_set)

# net_amount > X
x=6000
condition2=df['net_amount']>x

# order_date within last N days (relative to max date )
df['order_date'] = pd.to_datetime(df['order_date']) # Convert to datetime
n=60  #last 60dyas
max_date=df['order_date'].max()
threshold = max_date - pd.Timedelta(days=n)
condition3=df['order_date'] > threshold

result=df[condition1 & condition2 & condition3]
print("Final Multiple Queries Output :\n",result)
print("Final Count of Output : \n",result.count())
print("Final Total Net Amount of Output : \n",result['net_amount'].sum())