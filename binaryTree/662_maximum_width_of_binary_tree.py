class Solution:
    # O(n) time | O(h) space - where n is the number of nodes and h is the height of tree
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left_most_ids = []
        
        def dfs(node: TreeNode, depth: int, id: int):
            if not node: return 0
            if depth == len(left_most_ids): 
                left_most_ids.append(id)
            
            shifted_id = id - left_most_ids[depth]
            
            return max(shift_id + 1, 
                       dfs(node.left, depth + 1, shifted_id * 2), 
                       dfs(node.right, depth + 1, shifted_id * 2 + 1))
    
        return dfs(root, 0, 0)
    