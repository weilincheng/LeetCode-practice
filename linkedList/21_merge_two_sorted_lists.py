class Solution:
    # O(n) time | O(1) space - where n is the length of l1 + l2
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1 != None:
            tail.next = l1
        elif l2 != None:
            tail.next = l2
        
        return dummy.next