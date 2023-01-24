class Solution:
    # O(n) time | O(1) space - where n is the length of bank array
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = deque([(start, 0)])
        seen = {start}
        
        while queue:
            curGene, steps = queue.popleft()
            if curGene == end:
                return steps
            
            for c in "ACGT":
                for i in range(len(curGene)):
                    nextGene = curGene[:i] + c + curGene[i + 1:]
                    if nextGene not in seen and nextGene in bank:
                        queue.append((nextGene, steps + 1))
                        seen.add(nextGene)
        
        return -1
        
