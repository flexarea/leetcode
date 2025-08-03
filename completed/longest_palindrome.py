def longest_palindrome(s):
    if len(s) < 1:
        return ""

    longest_sub = s[0]

    for i in range(len(s)):
        window = s[i]
        j = i+1
        while j < len(s):
            window += s[j]
            if window == window[::-1]:
                if len(window) > len(longest_sub):
                    longest_sub = window
            j += 1

    return longest_sub


print(longest_palindrome("babad"))
