class Solution1:
    # O(n) time | O(h) space - where n is the number of nodes and h is the tree height
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        ans = 0
        while stack:
            currNode, currSum = stack.pop()
            if not currNode: continue
            currSum = (currSum << 1) | currNode.val
            if not currNode.left and not currNode.right:
                ans += currSum
            else:
                stack.append((currNode.right, currSum))
                stack.append((currNode.left, currSum))
        return ans
            
class Solution2:
    # O(n) time | O(h) space - where n is the number of nodes and h is the tree height
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        ans = 0
        while stack:
            currNode, currSum = stack.pop()
            if not currNode: continue
            currSum = (currSum << 1) | currNode.val
            if not currNode.left and not currNode.right:
                ans += currSum
            else:
                stack.append((currNode.right, currSum))
                stack.append((currNode.left, currSum))
        return ans
            