class Solution:
    # O(n) time | O(1) space - where n is the length of the input list
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        
        odd, even = head, head.next
        evenHead = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenHead
        return head
