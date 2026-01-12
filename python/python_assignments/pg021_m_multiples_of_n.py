def find_m_multiples(n, m):
    multiples = []
    for i in range(1, m + 1):
        multiples.append(n * i)
    return multiples

print(find_m_multiples(5, 6))
print(find_m_multiples(3, 4))
print(find_m_multiples(7, 5))