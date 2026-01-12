def set_odd_bit(n):
    for i in range(0,len(bin(n))-2,2):
        n = n | (1<<i)
    return n
n=20
print(bin(n))
print(bin(set_odd_bit(20)))
