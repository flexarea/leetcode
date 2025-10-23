class Solution:
    def isValidSudoku(self, board):
        ROW, COL = 3, 3

        r_bound = 0
        c_bound = 0
        res = [[] for _ in range(len(board))]

        i = 0
        while i < len(board):  # stop after exploring last row
            seen = set()  # check for duplicate in every grid
            for r in range(r_bound, ROW):
                for c in range(c_bound, COL):
                    if board[r][c] in seen:
                        return False  # right? -> could be a tiny optimization as we stop there
                    res[i].append(board[r][c])
                    seen.add(board[r][c])
            if COL == len(board):
                ROW += 3
                r_bound += 3
                # reset column range
                c_bound = 0
                COL = 3
            else:
                # only increment column range
                c_bound += 3
                COL += 3
            i += 1
        # check for rows


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

new_s = Solution()
new_s.isValidSudoku(board)
