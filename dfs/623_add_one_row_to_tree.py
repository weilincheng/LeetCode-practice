class Solution:
    # O(n) time | O(n) space - where n is the number of nodes 
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        
        def dfs(root, depth):
            if not root: return 
            if depth == 2:
                temp = root.left
                root.left = TreeNode(val)
                root.left.left = temp
            
                temp = root.right
                root.right = TreeNode(val)
                root.right.right = temp
            
                return
        
            dfs(root.left, depth - 1)
            dfs(root.right, depth - 1)
        
        dfs(root, depth)
        
        return root

