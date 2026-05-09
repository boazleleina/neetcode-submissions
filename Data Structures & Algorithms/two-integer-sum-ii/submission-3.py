class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #instantiate the pointers
        l = 0
        r = len(numbers) - 1
        while l < r:
            #find the total of the numbers at the index of the pointer
            total = numbers[l] + numbers[r]
            #if total is smaller than the targer means we need bigger numbers
            if total < target:
                l += 1
            #if total is bigger than the target, we need smaller numbers
            elif total > target:
                r -= 1
            #if total is equal to targer, we found our values
            else:
                return [l+1,r+1]