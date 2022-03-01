class Solution:
    # O(n) time | O(n) space - where n is the length of the array 
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def constructBST(nums, bst, startIdx, endIdx):
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
            
            constructBST(nums, bst, startIdx, midIdx - 1)
            constructBST(nums, bst, midIdx + 1, endIdx)
            
            return bst
        
        return constructBST(nums, None, 0, len(nums) - 1)
