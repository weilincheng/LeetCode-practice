class Solution:
    # O(1) time | O(1) space
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, second = head, head
        for _ in range(n):
            second = second.next
        
        if second is None:
            return first.next
        
        while second.next is not None:
            second = second.next
            first = first.next
        
        first.next = first.next.next
        
        return head
