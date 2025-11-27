class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        curr_max = 0
        curr_idx = 0

        for right in range(1, len(prices)):
            difference = prices[right] - prices[left]
            if difference > curr_max:
                curr_max = difference
                curr_idx = right
            if difference < 0:
                left = right
        return curr_max
