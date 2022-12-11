// O(n) time | O(h) space 
func maxPathSum(root *TreeNode) int {
    ans := math.MinInt64
    calculateMaxPathSum(root, &ans)
    return int(ans)
}

func calculateMaxPathSum(node *TreeNode, ans *int) int {
    if node == nil {
        return math.MinInt64
    }

    leftMaxPathSum := MaxInt(0, calculateMaxPathSum(node.Left, ans))
    rightMaxPathSum := MaxInt(0, calculateMaxPathSum(node.Right, ans))

    if curMaxPathSum := leftMaxPathSum + rightMaxPathSum + node.Val; curMaxPathSum > *ans {
        *ans = curMaxPathSum
    }

    return MaxInt(leftMaxPathSum, rightMaxPathSum) + node.Val
}

func MaxInt(x, y int) int {
    if x > y {
        return x
    }
    return y
}

