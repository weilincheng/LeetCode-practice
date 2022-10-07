class MyCalendarThree:

    def __init__(self):
        self.booked = {}
    
    # O(n*nlog(n)) time | O(n) space - where n is the number of events booked
    def book(self, start: int, end: int) -> int:
        self.booked[start] = self.booked.get(start, 0) + 1
        self.booked[end] = self.booked.get(end, 0) - 1
        
        cur = res = 0
        
        for key in sorted(self.booked.keys()):
            cur += self.booked[key]
            res = max(res, cur)
        
        return res

