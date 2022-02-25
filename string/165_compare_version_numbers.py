class Solution:
    # O(n + m) time | O(n + m) space - where n, m are the length of the strings
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(v) for v in version1.split('.')]
        v2 = [int(v) for v in version2.split('.')]
        for i in range(max(len(v1), len(v2))):
            v1Val = v1[i] if i < len(v1) else 0
            v2Val = v2[i] if i < len(v2) else 0
            
            if v1Val > v2Val: 
                return 1
            elif v1Val < v2Val:
                return - 1
        return 0
        