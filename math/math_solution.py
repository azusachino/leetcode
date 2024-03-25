from typing import List
import math


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        to_check = [0] * (len(nums) + 1)
        for n in nums:
            to_check[n] = 1
        for i, to in enumerate(to_check):
            if to == 0:
                return i
        return -1

    def pivotInteger(self, n: int) -> int:
        l = 0
        r = n * (n + 1) // 2
        for i in range(1, n + 1):
            r -= i
            if l == r:
                return i
            l += i
        return -1

    def minOperations(self, k: int) -> int:
        """
        Find min(a + b), so that (a + 1) * (b + 1) >= k.
        """
        v = math.isqrt(k)
        return v + (k - 1) // v - 1


if __name__ == "__main__":
    solution = Solution()
    # nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    # nums = [0, 1]
    # print("v ", s.missingNumber(nums))
    print("pivotInteger", solution.pivotInteger(4))
