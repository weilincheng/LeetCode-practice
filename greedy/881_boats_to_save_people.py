class Solution:
    # O(nlog(n)) time | O(n) space - where n is the length of array
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        l, r = 0, len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                r -= 1
            l += 1
        
        return l
    