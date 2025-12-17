import re
def remove_digits(lst):
    lst1=[]
    for items in lst:
        if not re.search(r"\d",items):
            lst1.append(items)
    return lst1

lst=["abc","ab1","111","ABC"]
print(remove_digits(lst))