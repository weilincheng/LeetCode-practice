class BSTIterator:
    # O(h) time | O(h) space - where h is the height of the left subtree
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
            
    # O(1) time in average
    def next(self) -> int:
        res = self.stack.pop()
        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res.val

    # O(1) time
    def hasNext(self) -> bool:
        return len(self.stack) >= 1
        