class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        curr_max = 0
        count = 0
        left, right = 0, 0

        while right < len(s):
            if s[right] not in window:
                window.add(s[right])
                curr_max = max(curr_max, right - left + 1)
                right += 1
            else:
                window.remove(s[left])
                left += 1
        return max(count, curr_max)
