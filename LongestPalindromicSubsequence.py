class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0]*len(s)for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        

        for length in range(2,len(s)+1):
            for i in range(len(s)-length+1): 
                j = length+i-1

                if s[i]==s[j]:
                    dp[i][j] = 2+dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        
        return dp[0][len(s)-1]
