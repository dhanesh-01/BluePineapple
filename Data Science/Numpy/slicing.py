"""
# Slicing + Boolean Masking
# Create an array of 50 random integers between 1 and 100.
# Extract:
# all even numbers
# numbers divisible by 3 and > 50
# Replace values < 20 with 20 (without loops)
"""

import numpy as np

a1D=np.random.randint(1,101, size=50)
print(a1D,"\n")

# All Even Numbers : array[condition]
print("All Even Numbers :",a1D[a1D%2==0],"\n") 

# numbers divisible by 3 and > 50
condition=(a1D%2==0) & (a1D>50)
print(a1D[condition],"\n")

# Replace values < 20 with 20 (without loops)
condition=a1D<20
a1D[condition]=20
print(a1D,"\n")