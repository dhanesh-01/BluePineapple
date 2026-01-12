# Write a python function to check whether the given two integers have opposite sign or not.
def check_postive(n1,n2):
    return True if n1>=0<=n2 else False
print(check_postive(-1,-2))
print(check_postive(1,2))
print(check_postive(-1,2))
print(check_postive(1,-2))