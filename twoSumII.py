class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dic = {}

        for index, num in enumerate(numbers):
            if target - num in num_dic:
                return sorted([index+1, num_dic[target-num]])
            else:
                num_dic[num] = index + 1
        return []
