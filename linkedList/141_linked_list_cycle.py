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
