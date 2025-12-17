# Prog. 011 Write a python function to remove first and last occurrence of a given character from the string.
str=input("enter the string : ")
char=input("enter the char which you want to remove its first and last occurrence : ")

def remove_first_last_occurrence(str,char):
    f=str.find(char)
    l=str.rfind(char)
    if f==-1:
        return str
    new_str=str[0:f]+str[f+1:l]+str[l+1:]
    return new_str

print("after removing first and last char new String : ",remove_first_last_occurrence(str,char))