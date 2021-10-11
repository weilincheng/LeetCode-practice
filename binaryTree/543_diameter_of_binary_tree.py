# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time | O(h) space - where n is the number of nodes 
    # and h is the max height of the tree
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            
            res[0] = max(res[0], 2 + left + right)
            
            return 1 + max(left, right)
        
        dfs(root)
        return res[0]
    