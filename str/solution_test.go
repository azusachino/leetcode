package str

import (
	"fmt"
	"testing"
)

func TestCountSubstring(t *testing.T) {
	s := "abc"
	r := countSubstrings(s)
	fmt.Printf("result is %d", r)
	if r != 3 {
		t.Error("wrong result")
	}
}
