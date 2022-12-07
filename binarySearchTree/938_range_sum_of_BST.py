class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def traverse(node):
            if not node: return 0
            
            rangeSum = 0
            if low <= node.val <= high:
                rangeSum += node.val
            
            if node.left and node.val > low:
                rangeSum += traverse(node.left)
            
            if node.right and node.val < high:
                rangeSum += traverse(node.right)
            
            return rangeSum
        
        return traverse(root)
