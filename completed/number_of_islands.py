class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        from collections import deque
        visited = set()
        island = 0
        ROW, COL = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))

            # right, left, up, down
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

            while q:
                row, col = q.popleft()
                for rd, cd in directions:
                    r, c = rd + row, cd + col
                    if (r in range(ROW) and
                            c in range(COL) and
                            (r, c) not in visited and
                            grid[r][c] == "1"
                            ):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    island += 1
        return island
