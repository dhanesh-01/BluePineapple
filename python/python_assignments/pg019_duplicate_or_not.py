def check_duplicate(lst):
    return len(lst) != len(set(lst))

print("enter the integers elements :")
elements = list(map(int, input().split()))
if check_duplicate(elements):
    print("Duplicates found") 
else:
    print("No duplicates found")      