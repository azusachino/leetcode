package utils

type Numbers interface {
	int | int8 | int16 | int32 | int64 | float32 | float64
}

// comparable only supports == & !=

func Max[T Numbers](a, b T) T {
	if a > b {
		return a
	}
	return b
}

func Min[T Numbers](a, b T) T {
	if a < b {
		return a
	}
	return b
}
