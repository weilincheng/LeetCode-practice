class Solution:
    # O(n^2) time | O(1) space - where n is the length of the list
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = head
        while curr:
            curr_next = curr.next
            prev, nxt = dummy, dummy.next
            while nxt:
                if nxt.val > curr.val: break
                prev = nxt
                nxt = nxt.next
            prev.next = curr
            curr.next = nxt
            curr = curr_next
        return dummy.next
    