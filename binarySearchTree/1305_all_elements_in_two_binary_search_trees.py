class Solution:
    # O(nlog(n)) time | O(n) space 
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result = []
        def collect(root):
            if root:
                collect(root.left)
                result.append(root.val)
                collect(root.right)
        collect(root1)
        collect(root2)
        
        return sorted(result)
