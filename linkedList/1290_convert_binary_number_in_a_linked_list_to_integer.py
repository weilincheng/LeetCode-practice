class Solution:
    # O(n) time | O(1) space - where n is the length of the input list
    def getDecimalValue(self, head: ListNode) -> int:
        ans = head.val
        while head.next:
            ans = ans * 2 + head.next.val
            head = head.next
        return ans
    