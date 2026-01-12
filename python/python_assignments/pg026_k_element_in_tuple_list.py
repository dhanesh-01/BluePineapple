def check_k_elements_in_tuples(tuple_list, k):
    for tup in tuple_list:
        if k in tup:
            continue
        else:
            return False
    return True
tuple_list = [(1, 2), (1,3, 4), (1,5, 6)]
k=1
print(check_k_elements_in_tuples(tuple_list, k))

