class Solution:
    # O(n) time | O(n) space 
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res, nodeStack = 0, [root]
        while nodeStack:
            currentNode = nodeStack.pop()
            if currentNode:
                if currentNode.left and not currentNode.left.right and not currentNode.left.left:
                    res += currentNode.left.val
                nodeStack.append(currentNode.left)
                nodeStack.append(currentNode.right)
        return res
            