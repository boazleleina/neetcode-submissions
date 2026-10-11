class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #get the total sum of nums
        total = sum(nums)
        #if the total is an odd number then there's no way to divide the values 
        if (total % 2) != 0:
            return False
        
        target = total / 2

        #create a set of reachable sums
        reachable = set()
        reachable.add(0)

        for num in nums:
            new_set = set()
            for s in reachable:
                if s + num <= target:
                    new_set.add(s+num)

            reachable.update(new_set)
        
        return target in reachable