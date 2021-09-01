# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Traverse the node, if next node's value is equal to the given value, link the current node to the next next node
    # O(n) time | O(1) space - where n is the length of the input list
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        currentNode = head
        while currentNode != None and currentNode.next != None:
            if currentNode.next.val == val:
                currentNode.next = currentNode.next.next
            else: 
                currentNode = currentNode.next
        if head != None and head.val == val:
            head = head.next
        return head
        