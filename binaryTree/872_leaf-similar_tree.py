class Solution:
    # O(n) time | O(m) space
    # where n is the total number of tree nodes and m is the total number of leaf nodes
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafValues1 = []
        leafValues2 = []

        def dfs(node, leafValues):
            if not node.left and not node.right:
                leafValues.append(node.val)
            if node.left:
                dfs(node.left, leafValues)
            if node.right:
                dfs(node.right, leafValues)
        
        dfs(root1, leafValues1)
        dfs(root2, leafValues2)
        return leafValues1 == leafValues2

