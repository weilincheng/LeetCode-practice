class UndergroundSystem:
    # O(1) time | O(n + m) space
    # where n is the number of customer, and m is the number of distinct trips
    def __init__(self):
        self.customerMap = {}
        self.timeMap = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customerMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, checkInTime = self.customerMap.pop(id)
        trip = startStation + '_' + stationName
        if trip not in self.timeMap:
            self.timeMap[trip] = (t - checkInTime, 1)
        else:
            curTime, tripNum = self.timeMap[trip]
            curTime, tripNum = curTime + (t - checkInTime), tripNum + 1
            self.timeMap[trip] = (curTime, tripNum)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip = startStation + '_' + endStation
        curTime, tripNum = self.timeMap[trip]
        return curTime / tripNum
