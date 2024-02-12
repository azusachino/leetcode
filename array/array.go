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
