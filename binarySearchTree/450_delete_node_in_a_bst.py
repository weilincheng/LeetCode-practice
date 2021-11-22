# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(h) time | O(h) space - where h is the height of tree
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is not None and root.right is not None:
                min = root.right
                while min.left is not None: min = min.left
                root.val = min.val
                root.right = self.deleteNode(root.right, min.val)
            else:
                return root.right if root.left is None else root.left
        return root
