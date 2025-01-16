def removeDuplicates(nums):
    left_pointer = 0
    prev = 0
    k = 0
    for i in range(len(nums)-1):
        identical = True
        prev = i
        for j in range(len(nums) - 2):
            c = 0
            rep = 0
            if nums[j+1] == nums[prev] and identical:
                if c < 3:
                    c += 1
                else:
                    left_pointer = j+1
                    prev = left_pointer
                    k += 1
                    identical = False
            else:
                if nums[j+1] != nums[prev]:
                    if rep:  # check if we are already checking for a specific number
                        # check if number we currently at is equal to number we are looking for
                        if nums[j+1] == rep:
                            if c < 2:
                                c += 1
                                # replace value pointed by left_pointer
                                nums[left_pointer] = nums[j+1]
                                left_pointer += 1
                                k += 1
                            else:
                                left_pointer = j+1
                                k += 1
                                prev = left_pointer
                        else:
                            # restart on new number
                            rep = 0
                            c = 0
                    else:
                        rep = nums[j+1]
                        nums[left_pointer] = nums[j+1]
                        left_pointer += 1
                        c += 1


print(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
print(removeDuplicates([1, 1]))
print(removeDuplicates([1, 2]))
print(removeDuplicates([1, 2, 2, 2]))
