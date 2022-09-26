# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n^2) time | O(h) space - where n is the number of tree nodes and h is the height of tree
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(node, curSum, curPath):
            if not node: return
            
            curPath.append(node.val)
            curSum += node.val
            if not node.left and not node.right and curSum == targetSum:
                res.append(curPath.copy())
            
            backtrack(node.left, curSum, curPath)
            backtrack(node.right, curSum, curPath)
            curPath.pop()
            
        backtrack(root, 0, [])
        
        return res

