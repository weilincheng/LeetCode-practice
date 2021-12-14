class Solution:
    # O(n) time | O(n) space - where n is the number of nodes of BST
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if not root: return None
            if low <= root.val <= high:
                self.ans += root.val
            if root.left and root.val > low:
                dfs(root.left)
            if root.right and root.val < high:
                dfs(root.right)
        self.ans = 0
        dfs(root)
        return self.ans
    