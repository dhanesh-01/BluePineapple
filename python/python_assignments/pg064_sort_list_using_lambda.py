# Write a function to sort a list of tuples using lambda.
def lambda_sort(lst):
    lst=sorted(lst,key=lambda x:x[0])
    return lst
lst=[(1,2),(7,8),(4,5),(3,6),(2,1)]
print(lambda_sort(lst))