/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// O(n) time | O(1) space - where n is the number of nodes
func oddEvenList(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }
    odd := head
    even, evenHead := head.Next, head.Next

    for even != nil && even.Next != nil {
        odd.Next = even.Next
        even.Next = even.Next.Next
        odd = odd.Next
        even = even.Next
    }

    odd.Next = evenHead

    return head
}
