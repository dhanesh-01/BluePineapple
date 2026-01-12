import re

def split_str_at_lowercase(str):
    result = re.split(r'[a-z]+', str)
    if '' in result:
        result.remove('')
    return result
str=input("enter any mix lowercase and uppercase char of string : ")         
print(split_str_at_lowercase(str))