class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        curr = []
        mapping = {"2":"abc", "3":"def",
         "4":"ghi", "5": "jkl", "6":"mno", 
         "7": "pqrs", "8":"tuv", "9": "wxyz"}
        
        def backtracking(index):
            if index == len(digits):
                res.append("".join(curr))
                return
            
            for letter in mapping[digits[index]]:
                curr.append(letter)

                backtracking(index + 1)
                curr.pop()
            
            
            
        if digits:
            backtracking(0)
        return res    
            