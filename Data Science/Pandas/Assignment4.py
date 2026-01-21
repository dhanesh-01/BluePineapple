""" 
# 4. GroupBy Aggregations
# Group by city and compute:
# total orders
# unique customers
# total revenue (sum net_amount)
# average order value
# Sort by revenue desc and show top 10 cities .
"""
import pandas as pd

df=pd.read_csv("./orders.csv")

#Group by city and compute: total orders & unique customers & total revenue (sum net_amount) 
                           # &average order value
result = df.groupby('city').agg(
    total_orders=('order_id', 'count'),
    unique_customers=('customer_id', 'nunique'),
    total_revenue=('net_amount', 'sum'),
    average_order_value=('net_amount', 'mean')
)
print("Using Group By Final Output:\n",result)

# Sort by revenue desc and show top 10 cities .
city_revenue=df.groupby('city')['net_amount'].sum().reset_index(name='total_revenue')
sorted_df = city_revenue.sort_values(by='total_revenue',ascending=False)
print("Top 10 cities : \n",sorted_df)