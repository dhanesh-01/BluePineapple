# Input : arr[] = {1, 2, 4, 5, 6, 6, 8, 9}, target = 11
# Output : 9

def close_smallest_number(lst,n):
    lst=sorted(lst)
    diff=n-lst[0]
    index=0
    for i in range(1,len(lst)):
        if not lst[i] > n:
            if n-lst[i] < diff:
                diff=n-lst[i]
                index=i
        else:
            break
    return lst[index]

lst=[1, 2, 4, 5, 6, 6, 8, 9]
n=11
print("close smallest number to n : ",close_smallest_number(lst,n))

lst=[2, 5, 6, 7, 8, 8, 9, 15, 19, 22, 32]
n = 17
print("close smallest number to n : ",close_smallest_number(lst,n))