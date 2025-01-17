def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums), nums

    # index where to place the next number
    p = 2

    for i in range(2, len(nums)):
        if nums[i] != nums[p-2]:
            nums[p] = nums[i]
            p += 1

    return p, nums


print(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
print(removeDuplicates([1, 1]))
print(removeDuplicates([1, 2]))
print(removeDuplicates([1, 2, 2, 2]))
