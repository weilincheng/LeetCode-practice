class Solution:
    # O(n) time | O(n) space - where n is the number of tree nodes
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return root
        queue = deque([root])
        res = []
        while queue:
            qLen = len(queue)
            curLevel = []
            for _ in range(qLen):
                node = queue.popleft()
                curLevel.append(node.val)
                for childNode in node.children:
                    queue.append(childNode)
            res.append(curLevel)
        return res

