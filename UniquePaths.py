from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def find_paths(i,j):
            if 0<=i<m and 0<=j<n:
                if i==m-1 and j==n-1:
                    return 1
                else:
                    return find_paths(i,j+1)+find_paths(i+1,j)
            return 0
        return find_paths(0,0)
