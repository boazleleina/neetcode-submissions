class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #create path to hold the set of seen rows and columns
        path = set()

        #find the len of rows and cols
        rows, cols = len(board), len(board[0])

        #create the recursive function, it will take the row, col and index in the word
        def backtracking(r, c, i):
            #if length of i is equal to the word, we found all the cells
            if i == len(word):
                return True
            
            #check if the cell is within bounds
            if r < 0 or r>= rows or c < 0 or c >= cols:
                return False
            
            #check if the current cell matches the character
            if board[r][c] != word[i]:
                return False
            
            #check if the cell is already in the path
            if (r,c) in path:
                return False

            #the cell is valid so add it to the path
            path.add((r,c))

            #recurse through the neighbors, checking the next character
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

            #remove the cell from path to start over
            path.remove((r,c))

            return found
        
        for r in range(rows):
            for c in range(cols):
                if backtracking(r, c, 0):
                    return True
        return False