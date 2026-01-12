min_list=lambda input_list : min(input_list,key=len)
l=[[1,2,3],
   [1,2,3,4],
   [1,2]]
print(min_list(l))