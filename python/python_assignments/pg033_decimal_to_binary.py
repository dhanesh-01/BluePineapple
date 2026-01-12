def decimal_to_binary(num):
    binary=""
    while num:
        binary+=str(num%2)
        num //=2
    return binary[::-1]

print(decimal_to_binary(13))
print(decimal_to_binary(15))