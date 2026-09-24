class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #create the path set to hold already used cells
        path = set()

        rows, cols = len(board), len(board[0])

        def backtracking(r, c, i):
            # if the path works then word found
            if i == len(word):
                return True
            
            

            #ensure the cell is in bound
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            
            #check if the cell matches the letter we are looking for
            if board[r][c] != word[i]:
                return False
            
            #if the current cell is in path then not valid
            if (r,c) in path:
                return False
            
            #record the current cell 
            path.add((r, c))

            #recurse through all 4 neighbors check for the next character
            found = (
            #UP
            backtracking(r-1, c, i+1) or
            #DOWN
            backtracking(r+1, c, i+1) or
            #LEFT
            backtracking(r, c-1, i+1) or
            #RIGHT
            backtracking(r, c+1, i+1)
            )
            #remove from the path
            path.remove((r,c))

            return found
        
        for r in range(rows):
            for c in range(cols):
                if backtracking(r,c, 0):
                    return True
        return False
        
        




            