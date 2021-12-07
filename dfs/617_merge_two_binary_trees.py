class Solution:
    # O(m + n) time | O(m + n) space - where m, n is the size of the trees
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None 
        val1 = root1.val if root1 else 0
        val2 = root2.val if root2 else 0
        root = TreeNode(val1 + val2)
        
        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        
        return root
    