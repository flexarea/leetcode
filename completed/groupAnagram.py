# brute force solution
from collections import defaultdict


def groupAnagramsBruteForce(strs):
    if len(strs) == 0:
        return [[""]]

    result = []

    def isAnagram(s, t):
        if len(s) != len(t):
            return False
        count = {}

        for i, j in zip(s, t):
            count[i] = count.get(i, 0) + 1
            count[j] = count.get(j, 0) - 1

        for val in count.values():
            if val != 0:
                return False
        return True

    visited = set()
    curr = []
    for i in range(len(strs)):
        if strs[i] not in visited:
            visited.add(strs[i])
            curr.append(strs[i])
        else:
            continue  # skip if value has been processed
        for j in range(i+1, len(strs)):
            if strs[j] not in visited and isAnagram(curr[0], strs[j]):
                curr.append(strs[j])
                visited.add(strs[j])
        result.append(curr)
        curr = []  # clear curr
    return result


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def groupAnagram(strs):
    # defaultdict automatically creates a default value for a key if that key does not exist yet.
    anagram_group = defaultdict(list)

    for word in strs:
        # tuple are immutable sequences, so they can be dictionary keys
        key = tuple(sorted(word))
        anagram_group[key].append(word)
    return list(anagram_group.values())
