''' 
# Matrix Ops (Dot, Transpose, Identity)
# Generate two matrices A (3x4) and B (4x2).
# Compute A @ B.
# Verify properties: (A.T).T equals A; create identity matrix I and show A @ I (shape permitting).
'''

import numpy as np
matrix1=np.random.rand(3,4)
matrix2=np.random.rand(4,2)

# Computing matrix1 @ matrix2.
# print(matrix1 @ matrix2) #Inner dimensions match (4 == 4) result will be (3 ,2)

# Verify properties: (A.T).T equals A.
A=np.random.rand(3,4)
print("Before Transpose :",A.shape)
AT=A.T
print("After Transpose :",AT.shape)
ATT=AT.T
print("After Transpose of Transpose :",ATT.shape)
print("Is AT.T equal to A?", np.allclose(A, ATT))


# create identity matrix I and show A @ I (shape permitting).
print("Matrix A :",A)
I = np.eye(4)
print("Identity Matrix :", I)
result=A @ I
print("A @ I:", result)
print("Is A @ I equal to A?", np.allclose(A, result)) 
 



