def gcd(n1,n2):
    if n2==0:
        return n1
    else:
        return gcd(n2,n1%n2)

def gcd_array_elements(lst):
    n1=lst[0]
    for n2 in range(1,len(lst)):
        n1=gcd(n1,lst[n2])
    return n1
lst=[12,18,30]
print(lst," GCD : ",gcd_array_elements(lst))

lst=[24,36,48]
print(lst," GCD : ",gcd_array_elements(lst))