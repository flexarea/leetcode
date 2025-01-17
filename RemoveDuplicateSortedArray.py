def removeDuplicates(nums):
    left_pointer = 0
    prev = 0
    k = 0
    identical = True
    for i in range(len(nums)-1):
        c0 = 1
        for j in range(len(nums) - 2):
            rep = 0
            if nums[j+1] == nums[prev] and identical:
                if c0 < 3:
                    c0 += 1
                    k += 1
                else:
                    identical = False
            else:
                if nums[j+1] != nums[prev]:
                    if rep:  # check if we are already checking for a specific number
                        # check if number we currently at is equal to number we are looking for
                        if nums[j+1] == rep:
                            if c0 < 3:
                                nums[i] = nums[rep]
                                c0 += 1
                                k += 1
                            else:
                                identical = False
                                prev = left_pointer
                        else:
                            # restart on new number
                            k += 1
                    else:
                        rep = j+1
                        c += 1


print(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
print(removeDuplicates([1, 1]))
print(removeDuplicates([1, 2]))
print(removeDuplicates([1, 2, 2, 2]))
