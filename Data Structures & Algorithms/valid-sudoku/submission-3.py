class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #initiate the row
        row = defaultdict(set)
        #initiate the column
        column = defaultdict(set)
        #initiate the squares
        square = defaultdict(set)
        #loop through rows in the board
        for r in range(9):
            #loop through columns in the board
            for c in range(9):
                    #if the current value is "." pass
                    if board[r][c] == ".":
                        continue
                    #if the board[r][c] is  in row[r] 
                    # or board[r][c] is  in columns[c]
                    #or board[r][c] is  in squares[r//3, c//3]
                    if (board[r][c] in row[r]
                    or board[r][c] in column[c]
                    or board[r][c] in square[(r//3, c//3)]):
                        #return False
                        return False
                    
                    #append value in row[r], columns[c], and squares[r//3, c//3]
                    row[r].add(board[r][c])
                    column[c].add(board[r][c])
                    square[(r//3, c//3)].add(board[r][c])
        #return True
        return True