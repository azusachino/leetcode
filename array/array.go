package array

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
