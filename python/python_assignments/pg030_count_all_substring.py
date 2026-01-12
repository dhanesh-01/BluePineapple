def count_substring_same_start_end_char(str):
    subStrings=[]                           
    for start in range(0,len(str)):
        for end in range(start+1,len(str)):
            temp=str[start:end+1]
            if temp[0]==temp[-1]:
                subStrings.append(temp)
    return subStrings


str="abababa"
print(count_substring_same_start_end_char(str))