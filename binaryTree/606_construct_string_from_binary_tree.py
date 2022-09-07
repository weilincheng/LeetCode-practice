class Solution:
    # O(n) time | O(n) space - where n is the number of nodes
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []
        
        def dfs(root):
            if not root:
                return
            
            res.append("(")
            res.append(str(root.val))
            
            dfs(root.left)
            if not root.left and root.right:
                res.append("()")
            dfs(root.right)
            res.append(")")
            
        dfs(root)
        
        return "".join(res[1:-1])

