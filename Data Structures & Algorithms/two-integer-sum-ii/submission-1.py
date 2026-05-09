class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #instantiate left and right pointer
        l ,r = 0, len(numbers) - 1

        #loop until l and r are on the same index or r becomes less
        while l < r:
            #get the total of the current index
            total = numbers[l] + numbers[r]
            #check the current value of l and the current value of r
            # if the sum is less than the target we need a bigger l
            if total < target:
                l += 1
            #if the sum is greater than the targer we need a smaller r
            elif total > target:
                r -= 1
            #if the total and sum are equal return the values in the index
            else:
                return [l+1,r+1]
        #defensive programming, if none of them match return an empty list
        return []
            
            

