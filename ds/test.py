from collections import defaultdict, deque

n = 8
a = [(0, 1), (0, 3), (1, 2),
     (3, 4), (3, 7), (3, 6), (4, 2), (4, 5), (5, 2)]

# matrix
m = [[0]*n for _ in range(n)]

for u, v in a:
    m[u][v] = 1

# 1. Depth First Search


def dfs(matrix):
    seen = set()
    seen.add(0)

    stack = [0]

    while stack:
        curr = stack.pop()
        print(curr)
        for neighbor in range(n):
            if m[curr][neighbor]:
                if neighbor not in seen:
                    stack.append(neighbor)
                    seen.add(neighbor)
