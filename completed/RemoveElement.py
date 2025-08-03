def removeElement(nums, val):
    if len(nums) == 1:
        nums
    p1 = 0  # begining of the array (iterator)
    p2 = 0  # static pointer for replacement
    n = 0
    counter = 0
    while n < len(nums):
        if nums[p2] != val:  # p2 is non-value
            p2 += 1
            n += 1
            counter += 1
        else:
            p1 = n
            if nums[p1] != val:  # non-val element
                temp = nums[p2]
                nums[p2] = nums[p1]
                nums[p1] = temp
                counter += 1
                p2 += 1
                n += 1
            else:
                n += 1
    return counter, nums


print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
