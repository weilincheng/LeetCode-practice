// O(n) time | O(1) space - where n is nums.length
func removeDuplicates(nums []int) int {
    insertIdx := 1
    for idx, _ := range nums {
        if idx == 0 {continue}
        if nums[idx] != nums[idx - 1] {
            nums[insertIdx] = nums[idx]
            insertIdx++
        }
    }
    return insertIdx
}

