class Solution:
    # O(n) time | O(n) space - where n is the number of nodes
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head 
        nodeMap = {None: None}
        curr = head
        while curr:
            nodeMap[curr] = ListNode(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            nodeMap[curr].next = nodeMap[curr.next]
            nodeMap[curr].random = nodeMap[curr.random]
            curr = curr.next
        
        return nodeMap[head]
