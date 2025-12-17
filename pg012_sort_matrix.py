def sort_matrix(matrix):
    return sorted(matrix,key=sum)

m=[[3, 2, 1], [1, 2, 3], [4, 5, 6], [0, 0, 0]]
print(sort_matrix(m))  

