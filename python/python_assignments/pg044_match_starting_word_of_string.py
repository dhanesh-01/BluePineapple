# Write a function that matches a word at the beginning of a string.

import re
def match_start_word(str,word):
    word=re.escape(word)
    return "Word is present " if re.findall(rf'{word}',str) else "word is not present"
str=input("Enter the string : ")
word=input("Enter the word you want to find at beginning : ")
print(match_start_word(str,word))