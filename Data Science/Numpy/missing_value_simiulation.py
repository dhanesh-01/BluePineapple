"""
# Missing Values Simulation
# Create a 1D float array of size 40.
# Randomly turn 20% positions into np.nan.
# Compute mean ignoring NaNs.
# Replace NaNs with the median of non-NaN values.
"""
import numpy as np

array=np.random.rand(40)

# Randomly turn 20% positions into np.nan.
percent = 0.20
sample_size = int(array.size * percent)   #converting 20%
array.flat[np.random.choice(array.size, size=sample_size, replace=False)] = np.nan
print("After assigning : ",array)

# Compute mean ignoring NaNs.
mean_value = np.nanmean(array)
print("MEAN :",mean_value)


# Replace NaNs with the median of non-NaN values.
median_value = np.nanmedian(array)
print("Median :",median_value)
array[np.isnan(array)] = median_value
print("After replace NaNs with Median :",array)