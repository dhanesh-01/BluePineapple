def first_duplicate(lst):
    seen=set()
    for item in lst:
        if item in seen:
            return item
        seen.add(item)
    return None
print("enter the integers elements :")
lst=list(map(int,input().split()))
print("First duplicate element is:",first_duplicate(lst))