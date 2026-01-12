def nth_digit_in_fraction(num,deno,n):
    if num>deno:
        return 0
    reminder=str(abs(num/deno)).split(".")[1]
    return int(reminder[n-1:n])
    
num=int(input("Enter numerator part of fraction : "))
deno=int(input("Enter Denomenator part of fraction : "))
n=int(input("Enter the value of n : "))
print(nth_digit_in_fraction(num,deno,n))