"""
# Add Derived Columns
# Using quantity , unit_price , discount_pct :
# compute gross_amount = quantity * unit_price
# compute net_amount = gross_amount * (1 - discount_pct/100)
# Add a is_high_value flag ( net_amount > threshold ).
"""
import pandas as pd

df=pd.read_csv("./orders.csv")   #for reading csv files
print(df.head())

# Using quantity , unit_price , discount_pct :
# compute gross_amount = quantity * unit_price
df['gross_amount'] =df['quantity']*df['unit_price']
print("Gross Amount :\n",df['gross_amount'])

# compute net_amount = gross_amount * (1 - discount_pct/100)
df['net_amount'] =df['gross_amount']*(1-df['discount_pct']/100)
print("Net Amount :\n",df['net_amount'])

# Add a is_high_value flag ( net_amount > threshold ).
threshold=5000
df['is_high_value']= df['net_amount'] >threshold
print("After adding is_high_value Col :\n",df)

df.to_csv("./orders.csv")