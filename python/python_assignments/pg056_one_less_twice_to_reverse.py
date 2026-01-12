def is_one_less_twice_reverse(num):
    rev=int(str(num)[::-1])
    return True if num == (rev*2)-1 else False
print(is_one_less_twice_reverse(73))
print(is_one_less_twice_reverse(37))