def find_odd_occuring_times(lst):
    lst1=[]
    for ele in lst:
        if lst.count(ele) % 2 != 0:
                lst1.append(ele)
    return list(set(lst1))

lst=[1,2,3,2,3,5,6,3,5]
print(find_odd_occuring_times(lst))

