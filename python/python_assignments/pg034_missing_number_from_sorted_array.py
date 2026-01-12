def missing_number_from_sorted_array(lst):
    lst=sorted(lst)   #[1, 2, 3, 5]
    missing=[]
    l=len(lst)
    for i in range(1,lst[l-1]):
        if i not in lst:
            missing.append(i)
    return missing

lst=[1,2,3,5]
print("Missing Natural Numbers : ",missing_number_from_sorted_array(lst))