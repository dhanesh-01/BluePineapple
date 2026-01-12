def sort_int_string_in_list(lst):
    int_list=[]
    str_list=[]
    for item in lst:
        if type(item) is int:
            int_list.append(item)
        else:
            str_list.append(item)
    return int_list,str_list
lst=[1,'one',2,'two',3,'three',4,'four']
int_list,str_list = sort_int_string_in_list(lst)
print("Integers List : ",int_list)
print("Strings List : ",str_list)