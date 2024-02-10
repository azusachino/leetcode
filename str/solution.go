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
