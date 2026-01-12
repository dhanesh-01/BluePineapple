# Prog. 007 Write a function to find all words which are at least 4 characters long in a string by using regex.

import re   # for regex 

text="find all words are at least four characters long in this string"

def find_long_words(text):
    pattern = r'\b\w{4,}\b'  #set the regex pattern

    result=re.findall(pattern,text)
    return result

result=find_long_words(text)
print(result)

