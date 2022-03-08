class Solution:
    # O(n) time | O(1) space
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

class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head
        for _ in range(n):
            right = right.next
            
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        
        return dummy.next