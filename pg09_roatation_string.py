# Prog. 009 Write a python function to find the minimum number of rotations required to get the same string.
#rotation means moving 1st char to end of string and count until it matches with original

data=input("enter the string : ")

def min_rotation(s):
    rotation=s
    count=0
    i=0
    while i<len(s):
        rotation=rotation[1:]+rotation[0] 
        count +=1
        if rotation == s:
            break
        i+=1
    return count

print("minimum count to roatate string : ",min_rotation(data))