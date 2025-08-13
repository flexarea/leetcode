def longestConsecutive(nums):
    sorted_nums = sorted(nums)

    ptr1 = 0
    res = 0
    current_len = 0

    for i in range(len(sorted_nums)):
        if i == 0:
            ptr1 = i
            current_len = 1
        else:
            if sorted_nums[i] == sorted_nums[ptr1]:
                continue
            elif sorted_nums[i] == sorted_nums[ptr1] + 1:
                ptr1 = i
                current_len += 1
            else:
                ptr1 = i
                res = max(current_len, res)
                current_len = 1

    res = max(res, current_len)
    return res


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longestConsecutive(nums))
