# Write a function to find t-nth term of geometric series.
def nth_term_geometric_series(a,r,n):
    return a*(r**(n-1))
print(nth_term_geometric_series(2,2,5))