class Solution:
    # O(n^2) time | O(n^2) space - wehre n is the number of nodes
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = {}
        res = []

        def dfs(node):
            if not node:
                return "null"
            left = dfs(node.left)
            right = dfs(node.right)
            curSubtree = f"{node.val},{left},{right}"
            if curSubtree in seen and seen[curSubtree] <= 1:
                res.append(node)
            seen[curSubtree] = seen.get(curSubtree, 0) + 1
            return curSubtree
        
        dfs(root)
        return res
