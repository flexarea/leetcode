def majorityElement(nums):
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    majority = 0
    value = 0
    print(dic)
    for key in dic:
        if dic[key] > value:
            majority = key
            value = dic[key]
    return majority


# print(majorityElement([3, 2, 3]))
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
