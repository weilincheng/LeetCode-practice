class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            slow = head.next
            fast = head.next.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
        except:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
    