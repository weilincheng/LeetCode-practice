class Solution:
    # O(n) time | O(1) space - where n is the length of the list
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            nextPair = curr.next.next
            second = curr.next
            
            second.next = curr
            curr.next = nextPair
            prev.next = second
            
            prev = curr
            curr = nextPair
            
        return dummy.next
    