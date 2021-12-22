class Solution:
    # O(n) time | O(n) space - where n is the number of nodes
    def reorderList(self, head: Optional[ListNode]) -> None:
        # store nodes in an array
        nodeArr = []
        currentNode = head
        while currentNode:
            nodeArr.append(currentNode)
            currentNode = currentNode.next
        
        if len(nodeArr) <= 2:
            return head
        
        # reorder the linkedlist with two pointers to iterate the node in array
        left, right = 0, len(nodeArr) - 1
        while left < right - 1:
            nodeArr[left].next = nodeArr[right]
            nodeArr[right].next = nodeArr[left + 1]
            nodeArr[right - 1].next = None
            left, right = left + 1, right - 1

        return head

class Solution2:
    # O(n) time | O(1) space - where n is the number of nodes 
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        
        # reverse the second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second 
            second = tmp
        
        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
