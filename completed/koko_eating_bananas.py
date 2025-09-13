class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        low = 1
        high = max(piles)
        k = 0
        curr_res = math.inf

        while low <= high:
            k = low + (high - low) // 2
            total_h = 0
            for i in piles:
                total_h += math.ceil(i/k)
            if total_h <= h:
                curr_res = min(curr_res, k)
            if total_h > h:
                low = k + 1
            else:
                high = k - 1

        return curr_res
