def removeDuplicates(nums):
    if len(nums) == 1:
        return 1
    p1 = 0
    p2 = 0
    size = len(nums) - 1
    n = 0
    k = 0

    while n < size:
        if p1 == p2:
            p2 += 1
        else:
            if nums[p1] == nums[p2]:
                nums.remove(nums[p1])
                n += 1
                k += 1
            else:
                if p2 == len(nums) - 1:
                    k += 1
                p1 += 1
                p2 += 1
                n += 1
                k += 1
    return k


print(removeDuplicates([1, 2]))
