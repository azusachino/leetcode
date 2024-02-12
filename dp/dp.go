package dpv1

func cherryPickup(grid [][]int) int {
	// setting up DP 3d data structure
	// first dimension indicates row,
	// second and third is about position of robots in a row
	// the value is the maximum that can be achieved
	// -1 indicates that configuration has not been explored
	var dp = make([][][]int, len(grid))
	for r := range dp {
		dp[r] = make([][]int, len(grid[0]))
		for a := range dp[r] {
			dp[r][a] = make([]int, len(grid[0]))
			for b := range dp[r][a] {
				dp[r][a][b] = -1
			}
		}
	}
	return _dfs(grid, dp, 0, 0, len(grid[0])-1)
}

func _dfs(grid [][]int, dp [][][]int, r, a, b int) int {
	if r == len(grid) || a < 0 || b < 0 || a == len(grid[0]) || b == len(grid[0]) {
		return 0
	}
	// solved combination
	if dp[r][a][b] != -1 {
		return dp[r][a][b]
	}

	// index from next level
	for offs1 := -1; offs1 <= 1; offs1++ {
		for offs2 := -1; offs2 <= 1; offs2++ {
			dp[r][a][b] = max(dp[r][a][b], _dfs(grid, dp, r+1, a+offs1, b+offs2))
		}
	}
	dp[r][a][b] += grid[r][a]
	// check, whether two robots are in the same cell
	if a != b {
		dp[r][a][b] += grid[r][b]
	}
	return dp[r][a][b]
}
