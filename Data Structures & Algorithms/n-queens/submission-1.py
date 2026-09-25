class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set ()
        posDiag = set()
        negDiag = set()

        board = [["."] * n for _ in range(n)]
        res = []

        def backtracking(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row+col) in negDiag or (row-col) in posDiag:
                    continue
                board[row][col] = "Q"
                cols.add(col)
                posDiag.add((row-col))
                negDiag.add((row+col))
                backtracking(row+1)
                board[row][col] = "."
                cols.remove(col)
                posDiag.remove((row-col))
                negDiag.remove((row+col))

        backtracking(0)
        return res
                
        