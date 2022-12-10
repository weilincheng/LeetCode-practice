// O(n) time | O(n) space 
func maxProduct(root *TreeNode) int {
    MOD := math.Pow(10, 9) + 7
    totalSum := sum(root)
    ans := 0
    traverse(root, totalSum, &ans)
    return ans % int(MOD)
}

func sum(node *TreeNode) int {
    if node == nil {
        return 0
    }
    return node.Val + sum(node.Left) + sum(node.Right)
}

func traverse(node *TreeNode, totalSum int, ans *int) int {
    if node == nil {
        return 0
    }
    subSum := node.Val + traverse(node.Left, totalSum, ans) + traverse(node.Right, totalSum, ans)
    productSum := (totalSum - subSum) * subSum
    if productSum > *ans {
        *ans = productSum
    }
    return subSum
}
