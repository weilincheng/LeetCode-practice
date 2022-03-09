class Solution:
    # O(n) time | O(1) space 
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        dummy = ListNode(0, head)
        prev, tail = dummy, head
        
        while tail:
            if tail.next and tail.val == tail.next.val:
                while tail.next and tail.val == tail.next.val:
                    tail = tail.next
                prev.next = tail.next
            else:
                prev = prev.next
            tail = tail.next

        return dummy.next
    