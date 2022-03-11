class Solution:
    # O(n) time | O(1) space - where n is the length of the list
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0: return head
        
        tail, listLen = head, 1
        while tail.next:
            tail = tail.next
            listLen += 1
        
        k %= listLen  
        if k == 0:
            return head

        currNode = head
        for _ in range(listLen - k - 1):
            currNode = currNode.next
        
        tail.next = head
        head = currNode.next
        currNode.next = None
        
        return head
        