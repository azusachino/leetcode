package set

import "github.com/azusachino/leetcode/utils"

func longestConsecutive(nums []int) int {
	res, numMap := 0, make(map[int]int)

	for _, num := range nums {
		if numMap[num] == 0 {
			l, r, sum := 0, 0, 0
			if numMap[num-1] > 0 {
				l = numMap[num-1]
			}
			if numMap[num+1] > 0 {
				r = numMap[num+1]
			}
			// sum: length of the sequence n is in
			sum = l + r + 1
			numMap[num] = sum
			// keep track of the max length
			res = utils.Max(res, sum)
			// extend the length to the boundary(s) of the sequence
			// will do nothing if n has no neighbors
			numMap[num-l] = sum
			numMap[num+r] = sum
		}
	}

	return res
}
