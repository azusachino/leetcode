package str

func countSubstrings(s string) int {
	if len(s) == 0 {
		return 0
	}
	count := 0
	var helper = func(count *int, s string, l, r int) {
		for l >= 0 && r < len(s) && s[l] == s[r] {
			*count += 1
			l--
			r++
		}
	}
	for i := 0; i < len(s); i++ {
		// odd length
		helper(&count, s, i, i)
		// even length
		helper(&count, s, i, i+1)
	}
	return count
}

func firstPalindrome(words []string) string {
	for _, w := range words {
		if isPalindrome(w) {
			return w
		}
	}
	return ""
}

func isPalindrome(s string) bool {
	l, r := 0, len(s)-1
	for l < r {
		if s[l] != s[r] {
			return false
		}
		l++
		r--
	}
	return true
}
