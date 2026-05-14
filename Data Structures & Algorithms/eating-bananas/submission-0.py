class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #initialize high and low
        low, high = 1, max(piles)
        #initialize result
        result = max(piles)
        #run the loop while low is less than or equal to high:
        while low <= high:
            #calculate middle which is (low+high)//2
            middle = (low+high) // 2
            #calculate sum for all the piles divided by middle
            total = sum(math.ceil(p/middle) for p in piles)
            #check if sum <= h:
            if total <= h:
                #if it is then it's valid, assign the middle to result
                result = middle
                #reduces high to find if a smaller value is valid
                high = middle - 1
                #else:
            else:
                #low increases so sum becomes less
                low = middle + 1
        #return result
        return result