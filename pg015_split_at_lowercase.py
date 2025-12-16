# Prog. 015 Write a function to split a string at lowercase letters.

str=input("enter any mix lowercase and uppercase char of string : ")

def split_str_at_lowercase(str):
    s=str
    part=""
    result=[]

    for char in s:
        if 'a' <= char <= 'z':
            part+=char