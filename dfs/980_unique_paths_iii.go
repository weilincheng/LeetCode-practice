func uniquePathsIII(grid [][]int) int {
    ROWS, COLS := len(grid), len(grid[0])
    squares := 1
    startR, startC := 0, 0
    
    for r := 0; r < ROWS; r++ {
        for c := 0; c < COLS; c++ {
            if grid[r][c] == 0 {
                squares++
            } else if grid[r][c] == 1 {
                startR, startC = r, c
            }
        }
    }
    return backtrack(grid, startR, startC, squares)
}

func backtrack(grid [][]int, r int, c int, squares int) int {
    if r < 0 || r == len(grid) || c < 0 || c == len(grid[0]) || grid[r][c] == -1 {
        return 0
    }
    if grid[r][c] == 2 {
        if squares == 0 {
            return 1
        } else {
            return 0
        }
    }
    grid[r][c] = -1
    uniquePaths := backtrack(grid, r + 1, c, squares - 1) + backtrack(grid, r - 1, c, squares - 1) + backtrack(grid, r, c + 1, squares - 1) + backtrack(grid, r, c - 1, squares - 1)
    grid[r][c] = 0
    return uniquePaths
} 
