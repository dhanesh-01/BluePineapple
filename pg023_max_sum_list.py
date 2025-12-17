def max_sum_list(lst):
    if not lst:
        return 0
    return max(sum(sublist) for sublist in lst)
lst=[[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print("Maximum sum among the lists is:", max_sum_list(lst))