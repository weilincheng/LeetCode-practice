// O(n) time | O(h) space 
// where n is number of tree nodes and h is the height of tree
func rangeSumBST(root *TreeNode, low int, high int) int {
    if root == nil {
        return 0
    }

    rangeSum := 0
    if low <= root.Val && root.Val <= high {
        rangeSum += root.Val
    }

    if root.Val > low {
        rangeSum += rangeSumBST(root.Left, low, high)
    }

    if root.Val < high {
        rangeSum += rangeSumBST(root.Right, low, high)
    }

    return rangeSum
}
