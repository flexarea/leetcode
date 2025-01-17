def removeDuplicates(nums):
    left_pointer = 0
    prev = 0
    k = 0
    identical = True
    c0 = 1
    for i in range(len(nums)):
        if nums[i] == nums[prev]:
            if c0 < 3:
                c0 += 1
                k += 1
                break
        for j in range(i+1, len(nums)):
            rep = 0
            if nums[j+1] != nums[prev]:
                if rep:  # check if we are already checking for a specific number
                    if nums[j+1] == rep:
                        if c0 < 3:
                            nums[i] = nums[rep]
                            c0 += 1
                            k += 1
                        else:
                            prev = left_pointer
                    else:
                        k += 1
                else:
                    rep = j+1
                    c += 1


print(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
print(removeDuplicates([1, 1]))
print(removeDuplicates([1, 2]))
print(removeDuplicates([1, 2, 2, 2]))
