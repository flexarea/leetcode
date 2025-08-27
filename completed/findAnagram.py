from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str):
        dic_s_count = Counter(p)
        dic_s = Counter()
        res = []

        left = 0

        for right in range(len(s)):
            dic_s[s[right]] += 1

            # shrink window if it grows too big

            if right - left + 1 > len(p):
                dic_s[s[left]] -= 1
                if not dic_s[s[left]]:
                    del dic_s[left]
                left += 1
            if right - left + 1 == len(p) and dic_s_count == dic_s:
                res.append(left)
        return res
