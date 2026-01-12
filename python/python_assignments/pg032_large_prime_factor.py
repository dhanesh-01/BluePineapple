# Write a python function to find the largest prime factor of a given number.
def is_prime_number(num):
    for i in range(2,num//2):
        if num%i == 0:
            return False
    return True

def largest_prime_factor(num):
    prime_divisor_num=[]
    for i in range(2,num+1):
        if num%i == 0:
            if is_prime_number(i):
                prime_divisor_num.append(i)
    return max(prime_divisor_num)

num=18
print("Largest prime factor : ",largest_prime_factor(num))

num=97  #already prime num
print("Largest prime factor : ",largest_prime_factor(num))