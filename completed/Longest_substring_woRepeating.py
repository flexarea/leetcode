def lengthOfLongestSubstring(s):
    res = 0
    curr_len = 0
    seen = set()
    ptr1 = 0
    ptr2 = 0

    while ptr2 < len(s):
        if s[ptr2] not in seen:
            seen.add(s[ptr2])
            res = max(res, ptr2 - ptr1 + 1)
            ptr2 += 1
        else:
            seen.remove(s[ptr2])
            ptr1 += 1
    return res


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("aab"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("dvdf"))
