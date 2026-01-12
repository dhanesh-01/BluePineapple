import re
def lowercase_letter_sequence(str):
    return re.findall(r'[a-z]+_[a-z]+',str)
str="AABCSxyz_abcOPvuWww_eeRTtt_TT"
print(lowercase_letter_sequence(str))