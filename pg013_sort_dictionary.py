def sort_dict(input_dict):
    sorted_dict = dict(sorted(input_dict.items(), key= lambda item: item[1], reverse=True))
    return list(sorted_dict.keys())[0]

input_dict = {'apple': 7, 'banana': 2, 'cherry': 7, 'date': 3}
print(sort_dict(input_dict), " : ",input_dict[sort_dict(input_dict)] )