def division_first_even_odd_from_list(lst):
    even=[]
    odd=[]
    for num in lst:
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
    if even and odd:
        return even[0]/odd[0]
    else:
        return 0
lst=[4,8,55,14,16,9,10,5]
print(division_first_even_odd_from_list(lst))