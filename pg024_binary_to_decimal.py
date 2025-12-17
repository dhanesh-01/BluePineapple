def binary_to_decimal(binary):
    decimal = 0
    length = len(binary)

    for i in range(length):
        decimal += int(binary[i]) * (2 ** (length - i - 1))

    return decimal

print(binary_to_decimal("1011"))
print(binary_to_decimal("1101"))