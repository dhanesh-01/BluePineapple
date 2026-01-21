"""
# Time Series Rolling Window Stats
# Create a 1D array representing 365 days of random “daily sales”.
# Compute rolling 7-day mean and rolling 30-day mean using NumPy (nopandas).
# Detect days where sales are > (rolling_30_mean + 2*rolling_30_std)
"""
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view   


# Generating 365 random sales figures between 100 and 1000
sales_data = np.random.randint(100, 1001, size=365)

# Compute rolling 7-day mean and rolling 30-day mean using NumPy (nopandas).
window_7 = sliding_window_view(sales_data, window_shape=7)
rolling_7_mean = window_7.mean(axis=1)
print("\nRolling 7-Day MEAN : ",rolling_7_mean)

window_30 = sliding_window_view(sales_data,window_shape=30)
rolling_30_mean = window_30.mean(axis=1)
print("\nRolling 30-Day MEAN : ",rolling_30_mean)

# Detect days where sales are > (rolling_30_mean + 2*rolling_30_std)
rolling_30_std = window_30.std(axis=1)
aligned_sales = sales_data[29:]   # align with rolling window
condition = aligned_sales > (rolling_30_mean+2*rolling_30_std)
result=aligned_sales[condition]
print("\nDetected Days where sales are Greater than rolling 30 day mean+2*rolling 30 day std \n",result)