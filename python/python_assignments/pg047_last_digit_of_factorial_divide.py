def fact(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        p=1
        for i in range(1,n+1):
            p *= i
        return p
def last_digit_of_factorial_division(n1,n2):
    if not n2>=n1:
        return "B values should be greater than A "
    else:
        return int(str(fact(n2)//fact(n1))[-1:])
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
print("Last Digit of Factorial a divides Factorial b : ",last_digit_of_factorial_division(a,b))
