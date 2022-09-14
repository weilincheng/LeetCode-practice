class Solution:
    # O(n) time | O(h) space 
    # - where n is the number of tree nodes and h is the height of tree
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, path):
            if not node:
                return 0
            path = path ^ (1 << node.val)
            if not node.left and not node.right:
                return 1 if path & (path - 1) == 0 else 0
            
            return dfs(node.left, path) + dfs(node.right, path)
                
        return dfs(root, 0)
    
