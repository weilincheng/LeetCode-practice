class Solution:
    # O(n) time | O(log(n)) space - where n is the length of the array 
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def constructBST(bst, startIdx, endIdx):
            if startIdx > endIdx: 
                return None
            
            midIdx = startIdx + (endIdx - startIdx) // 2
        
            if not bst:
                bst = TreeNode(nums[midIdx])
            else:
                if nums[midIdx] < bst.val:
                    bst.left = TreeNode(nums[midIdx])
                    bst = bst.left
                else:
                    bst.right = TreeNode(nums[midIdx])
                    bst = bst.right
            
            constructBST(bst, startIdx, midIdx - 1)
            constructBST(bst, midIdx + 1, endIdx)
            
            return bst
        
        return constructBST(None, 0, len(nums) - 1)

class Solution2:
    # O(n) time | O(log(n)) space - where n is the length of the input array
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(startIdx, endIdx):
            if startIdx > endIdx:
                return None
            
            midIdx = startIdx + (endIdx - startIdx) // 2
            root = TreeNode(nums[midIdx])
            root.left = helper(startIdx, midIdx - 1)
            root.right = helper(midIdx + 1, endIdx)
            return root
        
        return helper(0, len(nums) - 1)
        