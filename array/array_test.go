package array

import (
	"sort"
	"testing"
)

// how to run gotest: go test -v -timeout 30s -run ^TestFurthestBuilding$ github.com/azusachino/leetcode/array

func TestLargestPerimeter(t *testing.T) {
	nums := []int{5, 5, 5}
	var helper = func(nums []int) int64 {
		sort.Ints(nums)
		var res int64
		n := len(nums)
		prefixSum := make([]int64, 0)
		for i := range nums {
			prefixSum = append(prefixSum, res)
			res += int64(i)
		}

		for i := n - 1; i > 1; i-- {
			if int64(nums[i]) < prefixSum[i] {
				return prefixSum[i] + int64(nums[i])
			}
		}
		return -1
	}
	helper(nums)
}

func TestFurthestBuilding(t *testing.T) {
	heights := []int{4, 2, 7, 6, 9, 14, 12}
	result := furthestBuilding(heights, 5, 1)
    t.Logf("r: %v\n", result)
}
