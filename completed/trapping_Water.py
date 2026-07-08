class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [None]*len(height)
        max_right = [None]*len(height)
        area = 0

        prefix = height[0]

        for i in range(len(height)):
            max_left[i] = prefix
            prefix = max(prefix, height[i])

        suffix = height[-1]
        for i in range(len(height)-1, -1, -1):
            max_right[i] = suffix
            suffix = max(suffix, height[i])

        for i in range(len(height)):
            trap_val = min(max_left[i], max_right[i]) - height[i]
            if trap_val > 0:
                area += trap_val
        return area
