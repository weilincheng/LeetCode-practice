class Solution:
    # O(h) time | O(1) space - where h is the height of BST
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        currNode, prevNode = root, TreeNode(None)
        while currNode:
            prevNode = currNode
            currNode = currNode.right if val > currNode.val else currNode.left
        if val > prevNode.val:
            prevNode.right = TreeNode(val)
        else:
            prevNode.left = TreeNode(val)
        return root
    