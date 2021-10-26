class Solution:
    # Iterative 
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        stack = [root]
        while len(stack) > 0:
            currentNode = stack.pop()
            currentNode.left, currentNode.right = currentNode.right, currentNode.left
            
            if currentNode.left is not None:
                stack.append(currentNode.left)
            
            if currentNode.right is not None:
                stack.append(currentNode.right)
        
        return root

    # Recursive  
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left) 
        self.invertTree(root.right)
        
        return root