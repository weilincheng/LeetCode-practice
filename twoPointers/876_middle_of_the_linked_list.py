class Solution:
    # O(n) time | O(1) space - where n is the number of nodes
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
    