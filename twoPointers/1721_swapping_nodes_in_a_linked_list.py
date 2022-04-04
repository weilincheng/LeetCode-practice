class Solution:
    # O(n) time | O(1) space - where n is the number of nodes
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node1, node2 = head, head
        for _ in range(1, k):
            node1 = node1.next
        
        node = node1
        while node.next:
            node = node.next
            node2 = node2.next
        
        node1.val, node2.val = node2.val, node1.val
        
        return head
