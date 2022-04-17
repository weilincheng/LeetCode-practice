class Solution:
    # O(n) time | O(h) space - where n is the number of nodes, and h is the height of tree
    def increasingBST(self, root: TreeNode, tail = None) -> TreeNode:
        if not root:
            return tail
        
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        
        return res
    