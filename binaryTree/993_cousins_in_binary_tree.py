# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time | O(h) space - where n is the number of nodes and the h is the depth of binary tree
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def preorder(root, parent, depth):
            if not root:
                return 
            if root.val == x:
                self.xParent = parent
                self.xDepth = depth
            if root.val == y:
                self.yParent = parent
                self.yDepth = depth
            preorder(root.left, root, depth + 1)
            preorder(root.right, root, depth + 1)
        preorder(root, None, 0)
        return self.xParent != self.yParent and self.xDepth == self.yDepth
    