def lengthOfLongestSubstring(s):

    if len(s) < 1:
        return 0
    n = len(s)

    window = ""
    longest_substring = ""

    for i in range(n):
        if s[i] in window:
            window = window[window.index(s[i]) + 1:]
        window += s[i]
        if len(window) > len(longest_substring):
            longest_substring = window
    return len(longest_substring)


print(lengthOfLongestSubstring(" "))
