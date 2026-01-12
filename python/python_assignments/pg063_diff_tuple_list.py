# Write a function to find the maximum difference between available pairs in the given tuple list.
def max_diff(lst):
    max=abs(lst[0][0]-lst[0][1])
    for i in range(1,len(lst)):
        if max<abs(lst[i][0]-lst[i][1]):
            max=abs(lst[i][0]-lst[i][1])
    return max
lst=[(1,2),(4,5),(8,3),(9,5)]
print("Max Diff: ",max_diff(lst))