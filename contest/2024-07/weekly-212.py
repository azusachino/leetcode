from typing import List


class Solution:
    """
    1629. Slowest Key
        https://leetcode.com/problems/slowest-key/description/
    1630. Arithmetic Subarrays
        https://leetcode.com/problems/arithmetic-subarrays/description/
    """

    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        prev = 0
        mx = 0
        res = ""
        for c, a in zip(releaseTimes, keysPressed):
            if c - prev > mx or (c - prev == mx and a > res):
                res = a
                mx = c - prev
            prev = c
        return res

    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        def check(nums, l, r):
            n = r - l + 1
            s = set(nums[l : l + n])
            a1, an = min(nums[l : l + n]), max(nums[l : l + n])
            d, mod = divmod(an - a1, n - 1)
            return mod == 0 and all((a1 + (i - 1) * d) in s for i in range(1, n))

        return [check(nums, left, right) for left, right in zip(l, r)]
