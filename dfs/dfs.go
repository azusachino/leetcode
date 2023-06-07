package dfs

var dir = [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}

func surroundedRegions(grid [][]rune) {
	if len(grid) == 0 {
		return
	}
	M, N := len(grid), len(grid[0])
	// sink all the 'O' on the edge
	for i := 0; i < M; i++ {
		srDfs(i, 0, grid)
		srDfs(i, N-1, grid)
	}

	for j := 0; j < N; j++ {
		srDfs(0, j, grid)
		srDfs(M-1, j, grid)
	}

	// sink all the 'O' to 'X' and restore all the '*' to 'O'
	for i := 0; i < M; i++ {
		for j := 0; j < N; j++ {
			if grid[i][j] == 'O' {
				grid[i][j] = 'X'
			} else if grid[i][j] == '*' {
				grid[i][j] = 'O'
			}
		}
	}
}

func srDfs(i, j int, grid [][]rune) {
	if i < 0 || i >= len(grid) || j < 0 || j >= len(grid[0]) {
		return
	}
	if grid[i][j] == 'O' {
		grid[i][j] = '*'
		for k := 0; k < 4; k++ {
			srDfs(i+dir[k][0], j+dir[k][1], grid)
		}
	}
}
