def find_even(lst):
    even_lst=list(filter(lambda x:x%2==0,lst))
    return even_lst

lst=[1,2,3,4,5,6,7,8,9]
print("Even Numbers : ",find_even(lst))