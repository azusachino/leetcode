# Array

## Prefix Sum

```go
func prefixSum(nums []int) []int {
    n := len(nums)
    ps := make([]int, n)

    // init index 0
    ps[0] = nums[0]

    for i:=1; i<n; i++ {
        ps[i] = ps[i-1]+nums[i]
    }
    return ps
}
```

- range sum queries `prefixSum[j]-prefixSum[i-1]`
- subarray sum equals
- zero sum subarrays
- maximum subarray sum
- staock prices and profit
- counting inversions
