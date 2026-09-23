class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtracking(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if total + candidates[j] > target:
                    break
                curr.append(candidates[j])
                backtracking(j+1, curr, total+candidates[j])
                curr.pop()
        
        backtracking(0, [], 0)
        return res
            
            