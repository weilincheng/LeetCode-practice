class Solution:
    # Use a hash table to store the encountered node
    # If the next node is in the hash table, return True
    # O(n) | O(n) space - where n is the length of the input linked list. 
    def hasCycle(self, head: ListNode) -> bool:
        currentNode = head
        seenNode = {}
        while currentNode != None and currentNode.next != None:
            if currentNode in seenNode:
                return True
            else:
                seenNode[currentNode] = True
            currentNode = currentNode.next
        return False

    # Use fast pointer to see if it can reach to a null and return False
    # Use slow pointer to see if it will be caught by the fast pointer 
    def hasCycle2(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
        
