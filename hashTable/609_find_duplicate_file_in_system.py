class Solution:
    # O(nx) time | O(nx) space - where n is the number of strins and x is the average length
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contentMap = defaultdict(list)
        
        for path in paths:
            filePath = path.split(" ")
            for file in filePath[1:]:
                name, content = file.split("(")
                contentMap[content].append(filePath[0] + '/' + name)
        
        return [i for i in contentMap.values() if len(i) > 1]

