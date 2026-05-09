class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a hashmap to hold the num and index
        diff_map = {}
        #loop through the list nums
        for i in range(len(nums)):
            #check the difference between target and nums
            complement = target - nums[i]
            #if difference in hashmap return complement index and current index
            if complement in diff_map.keys():
                return [diff_map[complement], i]
        #add the current number and index to hashmap
            diff_map[nums[i]] = i
     