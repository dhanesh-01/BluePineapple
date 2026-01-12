# Write a python function to find the difference between sum of even and odd digits.
# ip=3471 op:10 

def diff_sum_even_odd(num):
    even_sum=0
    odd_sum=0
    while num!=0:
        if (num%10) % 2==0:
            even_sum += (num%10)
            num=num//10
        else:
            odd_sum += (num%10)
            num=num//10
        
    return even_sum/odd_sum
print(diff_sum_even_odd(3471))
