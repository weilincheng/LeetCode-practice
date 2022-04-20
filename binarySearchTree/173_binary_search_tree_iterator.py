class BSTIterator:
    # O(n) time | O(n) space - where n is the number of nodes
    def __init__(self, root: Optional[TreeNode]):
        stack, node = [], root
        self.Nodes = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            
            node = stack.pop()
            self.Nodes.append(node)
            node = node.left
    # O(1) time | O(1) space 
    def next(self) -> int:
        return self.Nodes.pop().val
        
    # O(1) time | O(1) space 
    def hasNext(self) -> bool:
        return len(self.Nodes) >= 1
        