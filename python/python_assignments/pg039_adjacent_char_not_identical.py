from collections import Counter
def is_rearrange_adjacent_char_possible(str):
    if max(Counter(str).values()) > round((len(str)+1)/2):
        return False
    else:
        return True
str="aaabb"
print("Rearrange Is possible to adjacent char are diff : ",is_rearrange_adjacent_char_possible(str))

