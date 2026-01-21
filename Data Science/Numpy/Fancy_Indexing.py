""" 
# Fancy Indexing + Scatter Update
# Create a length-30 zero array.
# Randomly pick 8 unique positions and set them to 1.
# Then set positions divisible by 5 to 9 (overwriting if needed).
"""
import numpy as np 

array=np.zeros(30)
print(array)

# Randomly pick 8 unique positions and set them to 1.
array.flat[np.random.choice(array.size, 8, replace=False)] = 1
print("After assigning : ",array)

# set positions divisible by 5 to 9 (overwriting if needed).
array[np.where(np.arange(array.size) % 5 == 0)]=9
print("set positions divisible by 5 to 9 : ",array)
