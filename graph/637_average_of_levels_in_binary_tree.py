class Solution:
    # O(n) time | O(n) space - where n is the number of tree nodes 
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = collections.deque([root])
        res = []
        while queue:
            qLen = len(queue)
            levelSum = 0
            for _ in range(qLen):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                levelSum += node.val
            res.append(levelSum / qLen)
        
        return res
    
