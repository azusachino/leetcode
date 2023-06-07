package bitwise

import "math/bits"

func minFlips(a int, b int, c int) int {
	res := 0

	for a > 0 || b > 0 || c > 0 {
		// if c's last bit is 0, we need a and b's last bit to be 0
		if c&1 == 0 {
			if a&1 == 1 {
				res++
			}
			if b&1 == 1 {
				res++
			}
			// if c's last bit is 1, we need a or b's last bit to be 1
		} else if a&1 == 0 && b&1 == 0 {
			res++
		}
		// shift right
		a, b, c = a>>1, b>>1, c>>1
	}

	return res
}

func minBitFlips(start int, goal int) int {
	return bits.OnesCount(uint(start ^ goal))
}

func evenOddBit(n int) []int {
	even, odd := 0, 0
	for i := 0; i < 32; i++ {
		// check current i-th bit is 1 or 0
		if (n & (1 << i)) != 0 {
			if i%2 == 0 {
				even++
			} else {
				odd++
			}
		}
	}
	return []int{even, odd}
}
