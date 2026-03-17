from collections import deque
from collections import defaultdict
a = [(0, 1), (0, 3), (1, 2),
     (3, 4), (3, 7), (3, 6), (4, 2), (4, 5), (5, 2)]


d = defaultdict(list)

for u, v in a:
    d[u].append(v)


source = 0
seen = set()
seen.add(source)

stack = [source]


# stack implementation
def dfs_stack(source):

    while stack:
        node = stack.pop()
        # process the element here
        print(node)
        for neighbor_node in d[node]:
            if neighbor_node not in seen:
                seen.add(neighbor_node)
                stack.append(neighbor_node)

# BFS implementation


q = deque()
q.append(source)


def bfs_queue(source):

    while q:
        node = q.popleft()
        # process the element here
        print(node)
        for neighbor_node in d[node]:
            if neighbor_node not in seen:
                seen.add(neighbor_node)
                q.append(neighbor_node)


bfs_queue(source)
