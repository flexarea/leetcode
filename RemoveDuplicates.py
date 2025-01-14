def removeDuplicates(nums):
    if len(nums) == 1:
        return nums
    p1 = 0
    p2 = 0
    n = 0

    while n < len(nums)-1:
        if p1 == p2:
            p2 += 1
        else:
            if nums[p1] == nums[p2]:
                nums.remove(nums[p1])
                n += 1
            else:
                p1 += 1
                p2 += 1
                n += 1
    return nums


print(removeDuplicates([0, 0, 1, 1, 2, 2, 3, 3, 4]))
