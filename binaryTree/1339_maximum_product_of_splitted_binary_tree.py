# O(n) time | O(n) space 
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7
        self.ans = totalSum = 0

        def total(node):
            if not node: return 0
            return node.val + helper(node.left) + helper(node.right)
        
        totalSum = total(root)

        def traverse(node):
            if not node: return 0
            subSum = node.val + traverse(node.left) + traverse(node.right)
            productSum = (totalSum - subSum) * subSum
            self.ans = max(self.ans, productSum)
            return subtreeSum
            
        traverse(root)

        return self.ans % MOD
