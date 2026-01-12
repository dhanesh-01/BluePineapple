def smallest(lst_digit):
    return list(filter(lambda x:x is int or x is float,min(lst_digit)))
print(smallest([5,1,2,7,9,4]))