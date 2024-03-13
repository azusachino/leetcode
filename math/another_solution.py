from typing import List
from math import gcd


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        sum = n * (n + 1) // 2
        """
        nums_sum = 0
        n = len(nums)
        total = n * (n + 1) // 2
        for n in nums:
            nums_sum += n
        return total - nums_sum

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        nums = set(nums)
        if 1 in nums:
            return False
        n = len(nums)
        if n == 1:
            return True
        nums = sorted(nums, reverse=True)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if gcd(nums[i], nums[j]) - 1:
                    nums[j] *= nums[i]
                    break
            else:
                return False
        return True


class AlternativeSolution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > mid:
                r = mid
            else:
                l = mid + 1
        return l
