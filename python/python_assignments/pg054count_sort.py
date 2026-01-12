def count_sort(lst):
    count_lst=[0]*(max(lst)+1)
    for i in lst:
        count_lst[i]+=1
    new_lst=[]
    for i,v in enumerate(count_lst):
        new_lst.extend([i]*v)       
    return new_lst

lst=[3,4,7,1,5,0,9]
print("Sorted using count sort : ",count_sort(lst))