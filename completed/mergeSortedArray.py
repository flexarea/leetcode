def merge(nums1, m, nums2, n):
    # Base case
    if n == 0:
        return nums1

    p1 = m - 1  # first pointer points to the largest (last) element of nums1
    # first pointer points to the first free space ('0') in nums1
    p2 = len(nums1)-1
    p3 = n-1  # third pointer points to largest element in nums2

    while n > 0:
        # max(nums1) < max(nums2)
        if nums1[p1] <= nums2[p3] and p1 >= 0:
            nums1[p2] = nums2[p3]
            p3 = p3 - 1
            p2 = p2 - 1
            n = n - 1
        else:
            # max(nums1) > max(nums2)
            # edge case
            if p1 < 0:
                nums1[p2] = nums2[p3]
                p3 = p3 - 1
                p2 = p2 - 1
                n = n - 1
            else:
                nums1[p2] = nums1[p1]
                nums1[p1] = 0
                p1 = p1 - 1
                p2 = p2 - 1
    return nums1


print(merge([2, 0], 1, [1], 1))
