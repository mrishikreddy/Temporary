class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        l = [-float('inf')]
        def dfs(node,l):
            if not node: 
                return 0
            
            left = max(0,dfs(node.left,l))
            right =max(0,dfs(node.right,l)) 
            l[0] = max(l[0],left+right+node.val)
            return max(left,right)+node.val
        dfs(root,l)
        return l[0]
