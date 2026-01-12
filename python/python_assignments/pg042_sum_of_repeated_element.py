from collections import Counter
def sum_repeated_element(lst):
    sum=0
    for key,value in Counter(lst).items():
        if value>1:
            sum=sum+(key*value)
    return sum

lst=[1,2,1,2,3,4,1,2]
print("Total Sum Of repeated Element : ",sum_repeated_element(lst))