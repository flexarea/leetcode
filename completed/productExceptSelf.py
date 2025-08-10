

def productExceptSelf(nums):
    answer = [None]*len(nums)
    left_prod = 1
    # left traversal
    for i in range(len(nums)):
        if i == 0:
            answer[i] = 1
        else:
            left_prod *= nums[i-1]
            answer[i] = left_prod

    # right traversal
    right_prod = 1
    for i in range(len(nums)-1, -1, -1):
        answer[i] *= right_prod
        right_prod *= nums[i]

    return answer


nums = [1, 2, 3, 4]
# expected = Output: [24,12,8,6]
print(productExceptSelf(nums))
