class Solution:
    # O(n) time | O(n) space - where n is the number of nodes
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.maxDiff = 0
        currMax = currMin = root.val
        
        def helper(root, currMax, currMin):
            if not root: return root
            currMax = max(currMax, root.val)
            currMin = min(currMin, root.val)
            self.maxDiff = max(self.maxDiff, currMax - currMin)
            helper(root.left, currMax, currMin)
            helper(root.right, currMax, currMin)
        
        helper(root, currMax, currMin)
        return self.maxDiff
        