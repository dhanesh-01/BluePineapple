def min_cost_path_with_path(cost, m, n):
    # Build min path matrix table
    min_cost = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    min_cost[0][0] = cost[0][0]

    # calculate all sum of First column vertically
    for i in range(1, m + 1):
        min_cost[i][0] = min_cost[i - 1][0] + cost[i][0]

    # calculate all sum of First row horizontally
    for j in range(1, n + 1):
        min_cost[0][j] = min_cost[0][j - 1] + cost[0][j]

    # Fill remaining cell in min_cost table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            min_cost[i][j] = cost[i][j] + min(
                min_cost[i - 1][j],      
                min_cost[i][j - 1],      
                min_cost[i - 1][j - 1]   
            )

    # Backtrack to find path
    path = []
    i, j = m, n

    while i > 0 or j > 0:
        path.append((i, j))

        # If at first row must come from left
        if i == 0:
            j -= 1
        # If at first column must come from top
        elif j == 0:
            i -= 1
        else:
            min_prev = min(
                min_cost[i - 1][j],
                min_cost[i][j - 1],
                min_cost[i - 1][j - 1]
            )

            if min_prev == min_cost[i - 1][j - 1]:
                i -= 1
                j -= 1
            elif min_prev == min_cost[i - 1][j]:
                i -= 1
            else:
                j -= 1

    # Add starting cell
    path.append((0, 0))
    path.reverse()

    return min_cost[m][n], path
cost = [
    [1, 2],
    [3, 4]
]

min_cost_matrix, path = min_cost_path_with_path(cost, 1, 1)

print("Minimum Cost:", min_cost_matrix)
print("Path:", path)
