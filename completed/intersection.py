def intersection(nums1, nums2):
    seen1 = {i for i in nums1}
    seen2 = {i for i in nums2}

    result = []

    for i in seen1:
        if i in seen2:
            result.append(i)

    return result


print(intersection([9, 4, 9, 8, 4], [4, 9, 5]))
