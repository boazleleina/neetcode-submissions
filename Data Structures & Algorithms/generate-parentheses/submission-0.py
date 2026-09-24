class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        para = []

        def backtracking(open_count, close_count):
            if len(para) == (2*n):
                res.append("".join(para))
                return
            
            if open_count < n:
                para.append("(")
                backtracking(open_count+1, close_count)
                para.pop()
            if close_count < open_count:
                para.append(")")
                backtracking(open_count, close_count+1)
                para.pop()
            

        
        backtracking(0, 0)
        return res