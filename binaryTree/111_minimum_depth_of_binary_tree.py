# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time | O(n) space - where n is the min depth of binary tree 
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        nodeQueue = collections.deque([[root, 1]])
        while nodeQueue:
            currentNode, currentDepth = nodeQueue.popleft()
            if currentNode:
                if not currentNode.left and not currentNode.right:
                    return currentDepth
                nodeQueue.append([currentNode.left, currentDepth + 1])
                nodeQueue.append([currentNode.right, currentDepth + 1])
            