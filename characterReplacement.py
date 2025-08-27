from collections import Counter


def characterReplacement(s: str, k: int) -> int:
    dic_s = {}
    res = 0

    if not s:
        return 0

    if len(s) == 1:
        return 1

    left = 0
    for right in s:
        print(dic_s)
        if right in dic_s:
            dic_s[right] += 1
        else:
            dic_s[right] = 1

        len_dic = sum(dic_s.values())
        if len_dic - max(dic_s.values()) <= k:
            res = max(res, len_dic)
        else:
            dic_s[s[left]] -= 1
            if not dic_s[s[left]]:
                del dic_s[s[left]]
            left += 1
    return res


print(characterReplacement("AABABBA", 1))
