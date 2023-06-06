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
