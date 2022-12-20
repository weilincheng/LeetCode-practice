class Solution:
    # O(V+E) time | O(V) space
    # where V is the number of vertices and E is the number of edges
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()

        def dfs(curRoom):
            visit.add(curRoom)
            for nextRoom in rooms[curRoom]:
                if nextRoom not in visit:
                    dfs(nextRoom)

        dfs(0)
        return len(visit) == len(rooms)
