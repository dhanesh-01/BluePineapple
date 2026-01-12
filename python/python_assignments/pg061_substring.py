# Write a python function to count number of substrings with the sum of digits equal to their length.
def digit_sum(num):
    num=int(num)
    sum=0
    while num!=0:
        sum+=num%10
        num//=10
    return sum 
def count_num_string(str):
    substr=""
    lst=[]
    for i in range(0,len(str)):
        substr=""
        for j in range(i,len(str)):
            substr+=str[j]
            if len(substr)==digit_sum(substr):       
                lst.append(substr)
            else:
                break
    return len(lst),lst
print(count_num_string("1121"))