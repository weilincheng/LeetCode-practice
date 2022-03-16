class Solution:
    # O(n) time | O(n) space - where n is the length of the input array
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, idx = [], 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[idx]:
                stack.pop()
                idx += 1
        return len(stack) == 0
