class Solution:
    # O(n) time | O(n) space - where n is the number of nodes in the input tree
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (0, 0)
            
            leftSum, leftTilt = dfs(root.left)
            rightSum, rightTilt = dfs(root.right)
            currentTilt = abs(leftSum - rightSum)
            
            return (leftSum + rightSum + root.val, leftTilt + rightTilt + currentTilt)
        
        return dfs(root)[1]
    