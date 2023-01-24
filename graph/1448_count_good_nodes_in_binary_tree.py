class Solution:
    # O(n) time | O(h) space - where n is the number of tree nods and h is the tree height
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxVal):
            if not root: return 0
            res = 1 if root.val >= maxVal else 0
            maxVal = max(root.val, maxVal)
            res += dfs(root.left, maxVal) + dfs(root.right, maxVal)
            return res
        
        return dfs(root, root.val)
    
