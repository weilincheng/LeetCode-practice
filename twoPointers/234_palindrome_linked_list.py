class Solution:
    # O(n) time | O(1) space - where n is the number of nodes
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the middle 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # Check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        
        return True
    
