# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time | O(n) space - where n is the number of nodes of binary tree
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nodeStack = [[root, 0]]
        res = 0
        while nodeStack:
            currentNode, currentNum = nodeStack.pop()
            if currentNode:
                currentNum += currentNode.val
                if not currentNode.left and not currentNode.right:
                    res += currentNum
                nodeStack.append([currentNode.left, currentNum * 10])
                nodeStack.append([currentNode.right, currentNum * 10])
        return res
    