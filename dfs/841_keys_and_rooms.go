// O(V+E) time | O(V) space 
// V is the number of vertices and E is the number of edges
func canVisitAllRooms(rooms [][]int) bool {
    visit := make(map[int]bool)
    dfs(0, visit, rooms)
    return len(visit) == len(rooms)
}

func dfs(room int, visit map[int]bool, rooms [][]int) {
    if _, ok := visit[room]; ok {
        return 
    }
    visit[room] = true
    for _, nextRoom := range rooms[room] {
        dfs(nextRoom, visit, rooms)
    }
}
