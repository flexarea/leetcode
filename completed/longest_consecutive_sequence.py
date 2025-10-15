class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        sorted_arr = sorted(set(nums))

        res = 1
        curr = 1

        for i in range(1, len(sorted_arr)):
            if sorted_arr[i-1] + 1 == sorted_arr[i]:
                curr += 1
            else:
                res = max(res, curr)
                curr = 1
        return max(res, curr)
