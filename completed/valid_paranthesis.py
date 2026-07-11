class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'}': '{', ')': '(', ']': '['}
        stack = []

        for i in s:
            if i in dic:
                if not stack or stack.pop() != dic[i]:
                    return False
            else:
                stack.append(i)
        return not stack
