class Solution:
    # O(n) time | O(n) space - where n is the number of nodes
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim(node):
            if not node: 
                return None
            if node.val > high:
                return trim(node.left)
            if node.val < low:
                return trim(node.right)

            node.left = None if node.val == low else trim(node.left)
            node.right = None if node.val == high else trim(node.right)
            return node
        
        return trim(root)
    