class Solution:
    # O(n) time | O(n) space - where n is the length of the input string
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        queue = deque()
        
        for indx, domino in enumerate(dom):
            if domino != ".": queue.append((indx, domino))
            
        while queue:
            indx, domino = queue.popleft()
            if domino == "L" and indx > 0 and dom[indx - 1] == ".":
                queue.append((indx - 1, "L"))
                dom[indx - 1] = "L"
            elif domino == "R":
                if indx + 1 < len(dom) and dom[indx + 1] == ".":
                    if indx + 2 < len(dom) and dom[indx + 2] == "L":
                        queue.popleft()
                    else:
                        queue.append((indx + 1, "R"))
                        dom[indx + 1] = "R"
        
        return "".join(dom)
    
