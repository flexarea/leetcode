class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1

        # Prefix product at an index is the product of all element on its left
        # res[0] should be 1  because there is no product on the left of res[0]
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # We do the same thing for sufix product (product of all element on the right)
        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            """
            the block below is equivalent to having a result2 array for postfix products of nums and doing:
            result2[i] = posfix
            postfix *= nums[i]

            But because we will end up multiplying result with result2, we can just directly multiply every postfix with the 
            same element at the index it would be multiplied with

            """
            res[i] *= postfix
            postfix *= nums[i]
        return res
