class Solution:
    # O(log(n)*log(n)) time | O(log(n)) space 
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)
    
    
    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)

