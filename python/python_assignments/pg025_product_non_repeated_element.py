import math
from collections import Counter
def product_non_repeated_element(lst):
    prod=[item for item in lst if lst.count(item)==1]
    return math.prod(prod)
print(product_non_repeated_element([1, 2, 3, 2, 4, 5, 1]))
print(product_non_repeated_element([7, 8, 9, 7, 10, 11, 8]))
    