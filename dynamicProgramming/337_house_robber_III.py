class Solution:
    # O(n) time | O(n) space - where n is the number of tree nodes
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return [0, 0]
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)
            
            withRoot = root.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair[0], leftPair[1]) + max(rightPair[0], rightPair[1])
            
            return [withRoot, withoutRoot]
        
        return max(dfs(root))
    