class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #   we want to combine position and speed into a single iterable of pairs
        #   we want to sort the iterable in ascending order then loop in backward
        pairs = sorted([(p, s) for p, s in zip(position, speed)])  # nlogn
        stack = []

        for p, s in pairs[::-1]:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
