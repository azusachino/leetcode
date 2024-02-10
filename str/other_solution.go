package str

func countSubstringsBruteForce(s string) int {
	res := 0
	isPalindrome := func(s string, l, r int) bool {
		for l < r {
			if s[l] != s[r] {
				return false
			}
			l += 1
			r -= 1
		}
		return true
	}
	n := len(s)
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			if isPalindrome(s, i, j) {
				res += 1
			}
		}
	}
	return res
}
