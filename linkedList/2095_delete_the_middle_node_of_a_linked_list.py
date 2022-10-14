class Solution:
    # O(n) time | O(1) space - where n is the length of the list
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return None
        
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        return head
    
