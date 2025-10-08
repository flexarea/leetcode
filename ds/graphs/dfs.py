# directed graph
from collections import defaultdict
a = [(0, 1), (0, 3), (1, 2),
     (3, 4), (3, 7), (3, 6), (4, 2), (4, 5), (5, 2)]

n = 8
m = [[0]*n for _ in range(n)]

# convert array of edges to adjacency matrix
for u, v in a:
    m[u][v] = 1
# print(edges)

# convert array of edges to adjacency list (recommended)

d = defaultdict(list)

for u, v in a:
    d[u].append(v)

# adjacency list is better because if you want to see what vertes is a single vertex connected to you can just use the key
# print(d[3])  # output [4, 7, 6] -> node 3 is connected to node 4,7,6
# print(m[3])  # oupt [0, 0, 0, 0, 1, 0, 1, 1] -> hard to decode


# DFS with Recursion - O(V + E) where v is the number of nodes and E is the number of edges

source = 0  # starting at node 0
seen = set()


def dfs_recursion(node):
    print(node)
    for neighbor in d[node]:
        if neighbor not in seen:
            seen.add(neighbor)
            dfs_recursion(neighbor)


# dfs_recursion(source)

# Iterative DFS with stack - O(V+E)
def dfs_stack(source):
    seen = set()
    seen.add(source)  # as soon as we see a new node, immediately add it to seen
    stack = [source]

    while stack:  # keep checking while there is still element in the stack
        node = stack.pop()
        print(node)

        for neighbor in d[node]:  # explore or traverse node we just popped from the stack
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)


dfs_stack(source)
