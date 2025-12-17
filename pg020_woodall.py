def is_woodall_number(num):
    n = 1
    while True:
        woodall = n * (2 ** n) - 1
        
        if woodall == num:
            return True
        if woodall > num:
            return False
        
        n += 1

print(is_woodall_number(7))    
print(is_woodall_number(23))   
print(is_woodall_number(10))   
