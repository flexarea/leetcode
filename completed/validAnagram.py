def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count = {}
    for char_s, char_t in zip(s, t):
        # increment value in s and decrement in t in the same dictionary (best space complexity)
        count[char_s] = count.get(char_s, 0) + 1
        count[char_t] = count.get(char_t, 0) - 1

    for var in count.values():
        # since incrementing and decrementing cancel out each character should have the value 0 if they are anagrams
        if var != 0:
            return False

    return True


s = "anagram"
t = "nagaram"

print(isAnagram(s, t))
