class Solution:
    # O(n) time | O(n) space - where n is the number of nodes 
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                potentialMatch = k - node.val
                if potentialMatch in seen:
                    return True
                seen.add(node.val)

                stack.append(node.left)
                stack.append(node.right)
        return False
