class Solution:
    # O(n) time | O(h) space - where n is the number of tree nodes and h is the height of the tree.
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root, left, right):
            if not root: 
                return True
            if not (root.val > left and root.val < right):
                return False
            
            return valid(root.left, left, root.val) and valid(root.right, root.val, right)
        
        return valid(root, float('-inf'), float('inf'))
