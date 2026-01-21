''' 1. Array Basics + Types
    # Create a 1D array of integers from 1 to 20.
    # Print: shape , dtype , min , max , sum , mean .
    # Convert it to float and show dtype change. 
'''

import numpy as np

a1D = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(a1D) 

print(a1D.shape) #for shape


'''
    # dtype is used to determine the type of an array.
'''
print("Before Changing the Data Type of Array",a1D.dtype)
a1D=np.array(a1D,dtype='f')  #it will covert it into float
print("After Changing the Data Type of Array",a1D.dtype)
a1D=np.array(a1D,dtype='i')
print(a1D.dtype)

# min, max, sum
print("minimum Value from 1D array : ",a1D.min())
print("maximum Value from 1D array : ",a1D.max())
print("Total sum of 1D Array : ",np.sum(a1D))
print("1D array MEAN: ",np.mean(a1D))