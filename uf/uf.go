package uf

import "github.com/azusachino/leetcode/tmpl"

func longestConsecutive(nums []int) int {
	N := len(nums)
	numMap, countMap, lcs, uf := make(map[int]int), make(map[int]int), 0, tmpl.UnionFind{}
	uf.Init(N)
	for i := 0; i < N; i++ {
		countMap[nums[i]] = i
	}

	for i := 0; i < N; i++ {
		if _, ok := numMap[nums[i]]; ok {
			continue
		}
		numMap[nums[i]] = i
		if _, ok := numMap[nums[i]-1]; ok {
			uf.Union(i, numMap[nums[i]-1])
		}

		if _, ok := numMap[nums[i]+1]; ok {
			uf.Union(i, numMap[nums[i]+1])
		}
	}

	for key := range countMap {
		parent := uf.Find(key)
		if parent != key {
			countMap[key]++
		}
		if countMap[parent] > lcs {
			lcs = countMap[parent]
		}
	}

	return lcs
}

func surroundedRegions(grid [][]rune) {
	if len(grid) == 0 {
		return
	}
	M, N := len(grid), len(grid[0])
	uf := tmpl.UnionFind{}
	// M*N+1 is the virtual node
	uf.Init(M*N + 1)

	for i := 0; i < M; i++ {
		for j := 0; j < N; j++ {
			if grid[i][j] != 'O' {
				continue
			}
			// if the node is on the edge, connect it to the virtual node
			if i == 0 || i == M-1 || j == 0 || j == N-1 {
				uf.Union(i*N+j, M*N)
				// if the node is not on the edge, connect it to its neighbors
			} else {
				if grid[i-1][j] == 'O' {
					uf.Union(i*N+j, (i-1)*N+j)
				}
				if grid[i+1][j] == 'O' {
					uf.Union(i*N+j, (i+1)*N+j)
				}
				if grid[i][j-1] == 'O' {
					uf.Union(i*N+j, i*N+j-1)
				}
				if grid[i][j+1] == 'O' {
					uf.Union(i*N+j, i*N+j+1)
				}
			}
		}
	}

	for i := 0; i < M; i++ {
		for j := 0; j < N; j++ {
			if uf.Find(i*N+j) != uf.Find(M*N) {
				grid[i][j] = 'X'
			}
		}
	}
}
