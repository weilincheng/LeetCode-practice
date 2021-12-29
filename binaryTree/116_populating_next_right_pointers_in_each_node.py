class Solution:
    # O(n) time | O(log(n)) space - where n is the number of nodes
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or not root.left: return root
            
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
            
        self.connect(root.left)
        self.connect(root.right)
    
        return root
