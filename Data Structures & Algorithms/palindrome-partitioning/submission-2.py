class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #create the result array
        res = []

        #the array to be updated each time
        curr = []

        def backtracking(start):
            #if start is the same length as string then it is a valid palindrome
            if start == len(s):
                res.append(curr.copy())
                return
            
            #check if the string is a palindrome, moving one character at a time
            for end in range(start+1, len(s)+1):
                if not self._palindrome(s[start:end]):
                    continue
                #append the current string to the array
                curr.append(s[start:end])
                #run the recursion
                backtracking(end)
                #pop from the array
                curr.pop()

        backtracking(0)
        return res
    

    #create a helper function to check the palindrome
    def _palindrome(self, st):
        l, r = 0, len(st)-1

        while l < r:
            if st[l] != st[r]:
                return False
            l += 1
            r -= 1
        return True