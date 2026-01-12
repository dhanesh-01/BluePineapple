def ways_to_tile_3xn(n):
    # If n is odd filling is impossible
    if n % 2 != 0:
        return 0

    # number of ways to fill dp = [0, 0, 0, 0, 0, 0, 0]
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 1   # empty board
    if n >= 2:
        dp[2] = 3

    # Apply the recurrence formula
    for i in range(4, n + 1, 2):
        dp[i] = 4 * dp[i - 2] - dp[i - 4]

    return dp[n]

print(ways_to_tile_3xn(2))  # 3
print(ways_to_tile_3xn(4))  # 11
print(ways_to_tile_3xn(6))  # 41
print(ways_to_tile_3xn(3))  # 0
