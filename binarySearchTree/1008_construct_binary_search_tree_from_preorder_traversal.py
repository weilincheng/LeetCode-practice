class Solution:
    # O(n) time | O(h) space
    # where n is the number of nodes, h is the height of tree
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(bound):
            if self.idx == len(preorder) or preorder[self.idx] > bound:
                return None
        
            root = TreeNode(preorder[self.idx])
            self.idx += 1
            root.left = helper(root.val)
            root.right = helper(bound)
            return root
        
        self.idx = 0
        return helper(float('inf'))
    