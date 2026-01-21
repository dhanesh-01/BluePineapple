"""
# Sorting + Top-K Without Full Sort
# Create 100 random numbers (floats).
# Find top 10 values and their indices using an efficient approach(argpartition).
# Print top 10 sorted descending (values + indices aligned).
"""
import numpy as np

numbers=np.random.rand(100)
print(numbers)

# Find top 10 values and their indices using an efficient approach(argpartition).
k=10  
top_indexes = np.argpartition(numbers, -k)[-k:]

# Print top 10 sorted descending (values + indices aligned).
top_indexes = top_indexes[np.argsort(numbers[top_indexes])[::-1]]
print(numbers[top_indexes], top_indexes)
