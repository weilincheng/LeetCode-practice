class Solution:
    # O(n) time | O(n) space - where n is the length of the input list
    def __init__(self, head: Optional[ListNode]):
        currentNode = head
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next
    # O(1) time
    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]
