import re
def lowercase_with_underscore(text):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, text)
text=input("enter text : ")         
print(lowercase_with_underscore(text))