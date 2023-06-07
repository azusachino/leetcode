package math

import (
	"math"
	"sort"

	"github.com/azusachino/leetcode/utils"
)

// sort and compare every slot
func canMakeArithmeticProgression(arr []int) bool {
	l := len(arr)
	sort.Ints(arr)
	for i := 2; i < l; i++ {
		if arr[i]-arr[i-1] != arr[i-1]-arr[i-2] {
			return false
		}
	}
	return true
}

// O(N), O(N), using set to help
func canMakeArithmeticProgression1(arr []int) bool {
	set := make(map[int]bool)
	mi, mx := math.MaxInt, math.MinInt
	for _, a := range arr {
		mi = utils.Min(a, mi)
		mx = utils.Max(a, mx)
		set[a] = true
	}
	N := len(arr)
	diff := mx - mi
	// should be (N-1) slots
	if diff%(N-1) != 0 {
		return false
	}
	// common difference
	d := diff / (N - 1)
	// check every slot
	for i := 0; i < N; i++ {
		if !set[mi+i*d] {
			return false
		}
	}
	return true
}

// 在 [1, n/2] 区间内搜索，只要有一组满足条件的解就 break。
func getNoZeroIntegers(n int) [2]int {
	for i := 1; i <= n/2; i++ {
		if !hasZero(i) && !hasZero(n-i) {
			return [2]int{i, n - i}
		}
	}
	return [2]int{}
}

func hasZero(n int) bool {
	for n > 0 {
		if n%10 == 0 {
			return true
		}
		n /= 10
	}
	return false
}
