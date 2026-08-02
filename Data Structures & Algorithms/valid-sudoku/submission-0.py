class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Row check
        for i in range(len(board)):
            check = set()
            for num in range(len(board)):
                if board[i][num] != '.':
                    if board[i][num] in check:
                        return False
                    check.add(board[i][num])
        
        # Column check
        for i in range(len(board)):
            check = set()
            for num in range(len(board)):
                if board[num][i] != ".":
                    if board[num][i] in check:
                        return False
                    check.add(board[num][i])
        
        # Grid check
        for startRow in range(0, 9, 3):
            for startCol in range(0, 9, 3):
                check = set()
                for row in range(startRow, startRow + 3):
                    for col in range(startCol, startCol + 3):
                        if board[row][col] == ".":
                            continue
                            
                        if board[row][col] in check:
                            return False
                            
                        check.add(board[row][col])
        
        return True
        