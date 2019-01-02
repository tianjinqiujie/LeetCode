class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue

                encoding = "r{}{}".format(r, board[r][c])
                if encoding in seen:
                    return False
                seen.add(encoding)

                encoding = "c{}{}".format(c, board[r][c])
                if encoding in seen:
                    return False
                seen.add(encoding)

                encoding = "{}{}{}".format(r // 3, c // 3, board[r][c])
                if encoding in seen:
                    return False
                seen.add(encoding)

        return True

b = [
  ["5","2",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
a = Solution().isValidSudoku(b)
print(a)