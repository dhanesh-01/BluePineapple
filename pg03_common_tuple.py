def find_similar_tuples(list1, list2):
    # If either list is empty
    if not list1 or not list2:
        return []

    # Convert first list into a set for fast lookup
    set1 = set(list1)

    # Find common tuples
    common_tuples = []
    for item in list2:
        if item in set1:
            common_tuples.append(item)

    return common_tuples
