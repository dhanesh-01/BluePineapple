def is_non_prime(n):
    # numbers <= 1 are non-prime
    if n <= 1:
        return True

    # Check divisibility from 2 to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True  # has a divisor → non-prime

    return False  # no divisors → prime


numbers = [-3, 0, 1, 2, 3, 4, 5, 9, 11]

for num in numbers:
    print(num, "→ Non-prime" if is_non_prime(num) else "→ Prime")