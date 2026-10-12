class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #if len(s1) + len(s2) does not equal to len(s3) then they can't be interleaved to form it
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [False] *(len(s2)+1)

        dp[0] = True

        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 and j==0:
                    continue
                #just came from s1
                match_s1 =  i > 0 and dp[j] and s1[i-1] == s3[i+j - 1]
                 
                #just came from s2
                match_s2 =  j>0 and dp[j-1] and s2[j-1] == s3[i+j - 1]
                  
                dp[j] = match_s1 or match_s2
        
        return dp[len(s2)]