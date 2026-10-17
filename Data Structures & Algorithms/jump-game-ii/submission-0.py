class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = current_end = jumps = 0

        for i in range(len(nums)-1):
            if i > farthest:
                break
            else:
                farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = farthest
        
        return jumps

            