def differ_by_one_bit(a, b):
    x = a ^ b
    return x != 0 and (x & (x - 1)) == 0
if differ_by_one_bit(1, 2):
    print("5 and 4 differ by one bit")
else:
    print("5 and 4 do not differ by only one bit")

print(differ_by_one_bit(3, 2))
print(differ_by_one_bit(5, 4))