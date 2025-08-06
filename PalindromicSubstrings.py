class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp = [[False]*len(s) for _ in range(len(s))]
        # count = 0

        # for i in range(len(s)):
        #     dp[i][i] = True
        #     count += 1
        
        # for length in range(2,len(s)+1):
        #     for i in range(len(s)-length+1):
        #         j = i+length-1

        #         if s[i]==s[j]:
        #             if length==2 or dp[i+1][j-1]:
        #                 count+=1
        #                 dp[i][j] = True

        # return count

        def expand(s,left,right):
            count = 0
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
            return count
        
        res = 0
        for i in range(len(s)):
            res += expand(s,i,i)
            res += expand(s,i,i+1)
        return res
