'''
# Broadcasting Practice
# Create a (4, 5) matrix of random floats.
# Create a (5,) vector and add it to every row using broadcasting.
# Python for Data Science - Assignments 2
# Normalize each row to sum to 1 (handle division carefully).
'''
import numpy as np

# Create a (4, 5) matrix of random floats.
matrix=np.random.rand(4,5)
print(matrix)

# Create a (5,) vector and add it to every row using broadcasting.
vector = np.array([1, 2, 3, 4, 5])
print(vector)
result= matrix+vector  #this brodcasting it add each vector element to each matrix col-wise elemnet 
print(result)

# Normalize each row to sum to 1 (handle division carefully).
row_sums = matrix.sum(axis=1, keepdims=True) #it compute row sums & keep dimensions for broadcasting)
row_sums[row_sums == 0] = 1   # it avoid division by zero
normalized = matrix / row_sums
print(normalized)
