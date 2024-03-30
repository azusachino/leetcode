from collections import Counter
from typing import List


class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = r = res = 0
        cur = 1
        while r < n:
            rn = nums[r]
            cur *= rn
            # Each step introduces x new subarrays, where x is the size of the current window (j - i + 1)
            while cur >= k and l <= r:
                ln = nums[l]
                l += 1
                cur //= ln
            res += (r - l) + 1
            r += 1
        return res

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        freq = Counter()
        l = r = 0
        while r < n:
            freq[nums[r]] += 1
            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                l += 1
            res = max(res, (r - l) + 1)
        return res

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        cur = 0
        res = n + 1
        while r < n:
            cur += nums[r]
            while cur >= target:
                res = min(res, (r - l) + 1)
                cur -= nums[l]
                l += 1
            r += 1
        return res

    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_ = max(nums)
        cur = res = 0
        l = r = 0
        while r < n:
            # count max_ occurrence
            cur += nums[r] == max_
            while cur >= k:
                cur -= nums[l] == max_
                l += 1
            # add all combinations from 0 ~ l
            res += l
            r += 1
        return res

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.at_most(nums, k) - self.at_most(nums, k - 1)

    def at_most(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        l = r = 0
        window = Counter()
        while r < n:
            window[nums[r]] += 1
            while len(window) > k:
                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    del window[nums[l]]
                l += 1
            res += r - l + 1
            r += 1
        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 1, 2, 3]
    print(solution.subarraysWithKDistinct(nums, 2))
