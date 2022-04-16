class Solution:
    # O(n) time | O(n) space - where n is the number of nodes 
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0
        
        def dfs(node):
            if node:
                dfs(node.right)
                self.total += node.val
                node.val = self.total 
                dfs(node.left)
            return node
        
        return dfs(root)
