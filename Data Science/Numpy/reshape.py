"""" 
# Reshape + Axis Operations
# Create an array from 1 to 60 and reshape into (5, 12).
# Compute:
# row-wise sums
# column-wise means
# global std
# Find the index of the maximum value in the 2D array.
"""
import numpy as np

a2D=np.arange(1,61)
print("Original Array : ",a2D)

#reshape the array
a2D=a2D.reshape(5,12)
print("after Reshape : ",a2D,"\n")

# row-wise sums
for row in a2D:
    print("Row-wise Sum : ",np.sum(row))

# column-wise means
num_col=a2D.shape[1]
for i in range(0,num_col):
    print(f'column {i+1} MEAN : {np.mean(a2D[:,i])}')

# global std
print(f'Global std : {np.std(a2D)}')

# Find the index of the maximum value in the 2D array.
rows, cols = np.where(a2D == np.max(a2D))
print(f'Maximum value Index({rows},{cols})') 