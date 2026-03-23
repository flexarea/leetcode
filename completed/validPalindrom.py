class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        if not s:
            return True
        clean_str = ""

        # first arrange string
        for char in s:
            if not char.isalnum():
                continue
            clean_str += char.lower()

        left, right = 0, len(clean_str)-1

        while left <= right:
            if clean_str[left] != clean_str[right]:
                return False
            left += 1
            right -= 1

        return True
