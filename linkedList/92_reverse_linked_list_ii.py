class Solution:
    # O(n) time | O(1) space - where n is the length of linked list
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev, cur = dummy, head
        for _ in range(left - 1):
            prev, cur = prev.next, cur.next
        
        nxt = cur.next
        for _ in range(right - left):
            temp = nxt.next
            nxt.next = cur
            cur, nxt = nxt, temp
        
        
        prev.next.next = nxt
        prev.next = cur
        
        return dummy.next
    
