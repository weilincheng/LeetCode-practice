class Solution:
    # O(nlog(n)) time | O(n) space - where n is the total number of nodes
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for head in lists:
            currNode = head
            while currNode:
                arr.append(currNode.val)
                currNode = currNode.next
        result = ListNode(0)
        currNode = result 
        for num in sorted(arr):
            currNode.next = ListNode(num)
            currNode = currNode.next
        return result.next
    