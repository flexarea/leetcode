class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        total = sum(piles)

        while low <= high:
            k = (low + high) // 2
            k_sum = 0
            for p in piles:
                k_sum += math.ceil(p/k)
            if k_sum > h:
                low = k + 1
            else:
                high = k - 1
        return low
