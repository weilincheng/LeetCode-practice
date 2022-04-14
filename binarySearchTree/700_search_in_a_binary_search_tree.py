# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Average: O(log(n)) time | O(log(n)) space - where n is the number of nodes in the BST
    # Worst: O(n) time | O(n) space 
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if val == root.val:
            return root
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
        return self.searchBST(root, val)

class Solution2:
    # O(log(n)) time | O(1) space - where n is the number of nodes 
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            else:
                root = root.left
        
        return None
        