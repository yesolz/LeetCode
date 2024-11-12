class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # row 검사
        for row in board:
            numSet = set()
            for c in range(0, 9):
                if row[c] == '.':
                    continue
                elif row[c] not in numSet:
                    numSet.add(row[c])
                else:
                    return False

        # col 검사
        for c in range(0, 9):
            numSet = set()
            for r in range(0, 9):
                if board[r][c] == '.':
                    continue
                elif board[r][c] not in numSet:
                    numSet.add(board[r][c])
                else:
                    return False

        # 3x3 검사
        for square in range(0, 9):
            numSet = set()
            for r in range(0, 3):
                for c in range(0, 3):
                    row = (square // 3) * 3 + r
                    col = (square % 3) * 3 + c
                    if board[row][col] == '.':
                        continue
                    elif board[row][col] not in numSet:
                        numSet.add(board[row][col])
                    else:
                        return False
        
        return True
