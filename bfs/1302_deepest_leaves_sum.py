class Solution:
    # O(n) time | O(n) space - where n is the number of nodes
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        levelSum = 0
        
        while q:
            qLen = len(q)
            levelSum = 0
            for _ in range(qLen):
                node = q.popleft()
                levelSum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return levelSum

