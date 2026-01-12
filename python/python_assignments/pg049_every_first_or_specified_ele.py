# Write a function to extract every first or specified element from a given two-dimensional list.
def extract_specified_element(lst,r=None,c=None):
    every_first=[]
    ele=0
    for i in range(0,len(lst)):
        every_first.append(lst[i][0])
        for j in range(0,len(lst[i])):
            if i==(r-1) and j==(c-1):
                ele=lst[i][j]
    if r==None and c==None:
        return every_first
    else:
        return ele
            

lst=[[1,2,3],
     [4,5,6],
     [7,8,9]]
print(extract_specified_element(lst,2,2))