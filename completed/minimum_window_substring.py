from collections import Counter


def minWindow(s, t):
    m, n = len(t), len(s)
    dic_t = Counter(t)
    dic_s = Counter(s[:m])  # substsring window
    # curr_substr = ""
    min_substr = s if n else ""
    min_found_flag = 0

    if m > n:
        return ""
    if n == m:
        return s if dic_s == dic_t else ""

    def checkSubsring(window_str):
        count = 0
        for key, value in dic_t.items():
            if key in window_str and window_str[key] >= value:
                count += 1
        return count

    left = 0

    # check for min substr here
    if checkSubsring(dic_s) == len(dic_t):
        min_substr = s[left:m]
        min_found_flag = 1

    for right in range(m, n):
        dic_s[s[right]] = dic_s.get(s[right], 0) + 1
        print(dic_s)
        # curr_substr += s[right]

        while checkSubsring(dic_s) == len(dic_t):
            window_str = s[left:right+1]
            if len(window_str) <= len(min_substr):
                min_substr = window_str
                min_found_flag = 1

            dic_s[s[left]] -= 1

            if dic_s[s[left]] == 0:
                del dic_s[s[left]]
            left += 1

    return min_substr if min_found_flag else ""


# s = "ADOBECODEBANC"
# t = "ABC"
s = "abc"
t = "ac"

print(minWindow(s, t))
