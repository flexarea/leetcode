def lengthOfLongestSubstring(s):
    res = 0
    curr_len = 0
    seen = set()
    ptr1 = 0
    ptr2 = 0

    while ptr2 < len(s):
        if s[ptr2] not in seen:
            seen.add(s[ptr2])
            curr_len += 1
            ptr2 += 1
        else:
            res = max(res, curr_len)
            curr_len = 1
            seen.remove(s[ptr2])
            ptr1 +=


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("aab"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("dvdf"))
