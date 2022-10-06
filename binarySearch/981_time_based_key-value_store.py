class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
    
    # O(M) time | O(M) space - where M is the number of set function calls
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
    
    # O(N*log(M)) time | O(1) space - where N is the number of get function calls 
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

