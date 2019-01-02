class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def dfs(board, stack):
            if not stack: return
            x, y = stack.pop()
            box = [board[x // 3 * 3 + i][y // 3 * 3 + j] for i in range(3) for j in range(3)]
            row = [board[x][j] for j in range(9)]
            col = [board[i][y] for i in range(9)]
            for i in "123456789":
                if not any([i in box, i in col, i in row]):
                    board[x][y] = i
                    dfs(board, stack)
                    if not stack: return
            board[x][y] = "."
            stack.append((x, y))

        stack = [(i, j) for i in range(9) for j in range(9) if board[i][j] == "."]
        dfs(board, stack)
        return board
b = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
a = Solution().solveSudoku(b)
print(a)