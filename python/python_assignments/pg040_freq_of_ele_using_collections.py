from collections import Counter
from itertools import chain
def find_freq(list_of_list):
    return Counter(chain.from_iterable(list_of_list))
list_of_list=[[1,2,3],[3,2,5],[5,8,1]]
print("Frequency : ",find_freq(list_of_list))

