class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image
        ROW, COL = len(image), len(image[0])

        def dfs(r, c):
            # check out of bond
            if r < 0 or r >= ROW or c < 0 or c >= COL:
                return

            # only change the ones
            if image[r][c] != original:
                return
            image[r][c] = color

            # right (0,1), left (0,-1), up(-1,0), down(1,0)
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r-1, c)
            dfs(r+1, c)
        dfs(sr, sc)
        return image
