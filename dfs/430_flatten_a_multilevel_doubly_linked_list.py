
class Solution:
    # O(n) time | O(n) space - where n is the number of nodes in doubly linked list. 
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        nodeStack, order = [head], []
        while nodeStack:
            last = nodeStack.pop()
            order.append(last)
            if last.next:
                nodeStack.append(last.next)
            if last.child:
                nodeStack.append(last.child)
                
        for i in range(len(order) - 1):
            order[i + 1].prev = order[i]
            order[i].next = order[i + 1]
            order[i].child = None
        return order[0]
