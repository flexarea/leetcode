# Two pointer optimal solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        [2,3,4]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return []
