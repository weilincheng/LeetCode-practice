class Solution:
    # O(n) time | O(h) space 
    # where n is the number of tree nodes and h is the height of tree
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            curSum = left + right + node.val
            ans[0] = max(ans[0], curSum)
            return max(left, right) + node.val

        ans = [float('-inf')]
        dfs(root)

        return ans[0] 

