class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

# More optimal (28ms)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        total = 0
        for i in range(len(sorted_nums)):
            left, right = i+1, len(sorted_nums)-1
            while left < right:
                curr_triplet_sum = sorted_nums[left] + \
                    sorted_nums[right] + sorted_nums[i]
                if 0 == curr_triplet_sum:
                    triplet = [sorted_nums[i],
                               sorted_nums[left], sorted_nums[right]]
                    if not triplet in res:
                        res.append(triplet)
                        left += 1
                        right -= 1
                    else:
                        left += 1
                        right -= 1
                elif curr_triplet_sum < 0:
                    left += 1
                else:
                    right -= 1
        return res
