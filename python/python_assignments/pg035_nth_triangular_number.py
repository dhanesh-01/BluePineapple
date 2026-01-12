def nth_triangular_number(n):
    if(n==0 or n<0):
        return 0
    return int((n*(n+1))/2)

n=int(input("enter n value to find nth Triangular Number : "))
print("Result : ",nth_triangular_number(n))