data = {"a": 5, "b": 2, "c": 9, "d": 1}

# descending order (sort based on value)

# bubble sort

items = list(data.items())
for i in range(len(items)):
    # - i because after every upper loop we have sorted element at len(item) - i and -1 because we are comparing with next element
    for j in range(len(items)-i-1):
        if items[j][1] > items[j+1][1]:
            items[j], items[j+1] = items[j+1], items[j]

# get the dictionary back
new_dic = dict(items)
# print(new_dic)

# python built-in method

another_dic = dict(
    sorted(data.items(), key=lambda item: item[1], reverse=True))
print(another_dic)
