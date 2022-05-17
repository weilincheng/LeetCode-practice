# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # O(n) time | O(n) space - where n is the number of nodes
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack1, stack2 = [original], [cloned]
        while stack1:
            node1, node2 = stack1.pop(), stack2.pop()
            if node1:
                if node1 == target:
                    return node2
            
                stack1.append(node1.left)
                stack1.append(node1.right)
                stack2.append(node2.left)
                stack2.append(node2.right)
