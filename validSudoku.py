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
                    if board[r][c] != "." and board[r][c] in seen:
                        return False  # right? -> could be a tiny optimization as we stop there
                    res[i].append(board[r][c])
                    if board[r][c] != ".":
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

        # check for valid rows
        ROW, COL = len(board), len(board[0])

        for r in range(ROW):
            row_set = set()  # create a new set to check the rows
            for c in range(COL):
                if board[r][c] != "." and board[r][c] in row_set:
                    return False
                if board[r][c] != ".":
                    row_set.add(board[r][c])

        # check for valid columns

        for r in range(ROW):
            col_set = set()
            for c in range(COL):
                if board[c][r] != "." and board[c][r] in col_set:
                    return False
                if board[c][r] != ".":
                    col_set.add(board[c][r])
        return True


board1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

new_s = Solution()
print(new_s.isValidSudoku(board))
