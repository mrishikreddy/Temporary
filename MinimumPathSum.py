class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        def dfs(grid,i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]):
                if i==len(grid)-1 and j==len(grid[0])-1:
                    return grid[i][j]

                if (i,j) in dp:
                    return dp[(i,j)]
                dp[(i,j)] = grid[i][j]+min(dfs(grid,i+1,j),dfs(grid,i,j+1))
                return dp[(i,j)]
            else:
                return float('inf')
        
        return dfs(grid,0,0)


# Optimized Code
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1,len(grid)): 
            grid[i][0] += grid[i-1][0]
        
        for i in range(1,len(grid[0])):
            grid[0][i] += grid[0][i-1]

        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])


        return grid[-1][-1]
