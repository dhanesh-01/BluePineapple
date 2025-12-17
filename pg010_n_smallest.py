def n_smallest(dataset,n):
    ds=sorted(dataset)
    return ds[:n]

dataset=[1,2,8,7,4,10,5,15,3]
print("how many smallest numbers you want to find ? ")
n=int(input())
print(f"{n} smallest numbers are : ",n_smallest(dataset,n))
