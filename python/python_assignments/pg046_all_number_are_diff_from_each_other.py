def check_all_num_diff(lst):
    return "All Elements different From each other" if len(lst)==len(set(lst)) else "No, Elements are not different From eacch other"

lst=list(map(int , input("Enter the number into list : ").split() ))
print(check_all_num_diff(lst))