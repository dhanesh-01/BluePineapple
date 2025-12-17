# C(n, k) = n! / (k! * (n-k)!) how many ways we can choose k items from n items.

def fact(num):
    if num==0:
        return 0
    else:
        p=1
        for i in range(1,num+1):
            p *= i
    return p

def binomial_coefficient(n,k):
    if k < 0 or k > n:
        return 0
    
    num=fact(n)
    den=fact(k) * fact(n-k)
    return num/den

n=int(input("enter value of n :"))
k=int(input("enter the value k : "))
print("Number of ways : ",binomial_coefficient(n,k))

