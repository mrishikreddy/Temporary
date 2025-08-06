class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        def dfs(node):
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            self.max_length = max(self.max_length,l+r)
            return 1+max(l,r)
        dfs(root)
        return self.max_length
