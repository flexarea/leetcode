# brute force solution
from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def groupAnagram(strs):
    # defaultdict automatically creates a default value for a key if that key does not exist yet.
    anagram_group = defaultdict(list)

    for word in strs:
        # tuple are immutable sequences, so they can be dictionary keys
        key = tuple(sorted(word))
        anagram_group[key].append(word)
    return list(anagram_group.values())
