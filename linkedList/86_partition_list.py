class Solution:
    # O(n) time | O(1) space - where n is the length of the linked list
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftTail = leftDummy = ListNode()
        rightTail = rightDummy = ListNode()
        while head:
            if head.val < x:
                leftTail.next = head
                leftTail = leftTail.next
            else:
                rightTail.next = head
                rightTail = rightTail.next
            head = head.next
        leftTail.next = rightDummy.next
        rightTail.next = None
        return leftDummy.next

