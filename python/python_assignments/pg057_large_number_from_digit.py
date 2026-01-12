# Write a python function to find the largest number that can be formed with the given digits.
def large_number(lst_digit):
    large_num=""
    lst_digit=sorted(lst_digit,reverse=True)
    for num in lst_digit:
        large_num+=str(num)
    return int(large_num)
lst=[1,2,8,9]
print("max num :",large_number(lst))
