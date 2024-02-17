package array

import (
	"container/heap"
	"sort"
)

// majorityElement len(nums) >= 1
func majorityElement(nums []int) int {
	// base case
	major, count := nums[0], 1
	for i := 1; i < len(nums); i++ {
		if count == 0 {
			count++
			major = nums[i]
		} else if major == nums[i] {
			count++
		} else {
			count--
		}
	}
	return major
	// other solution
	// 1. sort -> mid
	// 2. map -> count -> loop
}

func merge(nums1 []int, m int, nums2 []int, n int) {
	i, j, p := m-1, n-1, len(nums1)-1
	for i >= 0 && j >= 0 {
		if nums1[i] > nums2[j] {
			nums1[p] = nums1[i]
			i--
		} else {
			nums1[p] = nums2[j]
			j--
		}
		p--
	}
	// in case of leftover
	for j >= 0 {
		nums1[p] = nums2[j]
		j--
		p--
	}
}

func removeElement(nums []int, val int) int {
	if (len(nums)) == 0 {
		return 0
	}
	fast, slow := 0, 0
	for fast < len(nums) {
		if nums[fast] != val {
			nums[slow] = nums[fast]
			slow++
		}
		fast++
	}
	return slow
}

func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	fast, slow := 0, 0
	for fast < len(nums) {
		if nums[fast] != nums[slow] {
			// leave at least one occurrence
			slow++
			nums[slow] = nums[fast]
		}
		fast++
	}
	// count rather than index
	return slow + 1
}

// rearrangeArray check https://leetcode.com/problems/rearrange-array-elements-by-sign
func rearrangeArray(nums []int) []int {
	res := make([]int, len(nums))
	posIndex, negIndex := 0, 1
	for _, n := range nums {
		if n > 0 {
			res[posIndex] = n
			posIndex += 2
		} else {
			res[negIndex] = n
			negIndex += 2
		}
	}
	return res
}

// largestPerimeter https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/
func largestPerimeter(nums []int) int64 {
	sort.Ints(nums)
	var res int64

	n := len(nums)
	for i := 0; i < n; i++ {
		res += int64(nums[i])
	}

	for i := n - 1; i > 1; i-- {
		res -= int64(nums[i])
		if int64(nums[i]) < res {
			return res + int64(nums[i])
		}
	}
	return -1
}

// calculatePrefixSum
func calculatePrefixSum(nums []int) []int {
	n := len(nums)

	prefixSum := make([]int, n)

	// init
	prefixSum[0] = nums[0]

	for i := 1; i < n; i++ {
		prefixSum[i] = prefixSum[i-1] + nums[i]
	}

	return prefixSum
}

func findLeastNumOfUniqueInts(arr []int, k int) int {
	d := make(map[int]int)
	for _, v := range arr {
		d[v]++
	}
	var freq []int
	for _, v := range d {
		freq = append(freq, v)
	}
	sort.Ints(freq)
	for i := 0; i < len(freq); i++ {
		if k >= freq[i] {
			k -= freq[i]
			freq[i] = 0
		} else {
			return len(freq) - i
		}
	}
	return 0
}

func furthestBuilding(heights []int, bricks int, ladders int) int {
	h := &IntHeap{}
	heap.Init(h)
	for i := 1; i < len(heights); i++ {
		diff := heights[i] - heights[i-1]
		if diff > 0 {
			heap.Push(h, diff)
			// ladders exhausted, use bricks to cover (from small stairs)
			if h.Len() > ladders {
				bricks -= heap.Pop(h).(int)
			}

			if bricks < 0 {
				return i - 1
			}
		}
	}
	return len(heights) - 1
}

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
