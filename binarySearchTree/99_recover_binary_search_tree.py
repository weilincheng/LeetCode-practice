class Solution:
    # O(n) time | O(h) space - where h is the height of the tree
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        stack, drops = [], []
        node, prev = root, TreeNode(float('-inf'))
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            if prev.val > node.val:
                drops.append((prev, node))
            prev, node = node, node.right
                    
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val
        
        return root
   