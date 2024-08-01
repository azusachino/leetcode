from collections import Counter
from functools import cache
from typing import List


class Solution:
    """
    2024.06.16
    3184. Count Pairs That Form a Complete Day I
        https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/description/
    3185. Count Pairs That Form a Complete Day II
        https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/description/
    3186. Maximum Total Damage With Spell Casting
        https://leetcode.com/problems/maximum-total-damage-with-spell-casting/description/
    3187. Peaks in Array
        https://leetcode.com/problems/peaks-in-array/
    """

    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hours.sort()
        res = 0
        n = len(hours)
        for i in range(n):
            for j in range(i + 1, n):
                if (hours[i] + hours[j]) % 24 == 0:
                    res += 1
        return res

    # with larger data range 10**5
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        """
        (num1 + num2) % 24 = 0
        (num1 % 24 + num2 % 24) % 24 = 0

        Let x = num1 % 24 and y = num2 % 24 and 0 <= x, y < 24
        (x + y) % 24 = 0
        (24 - x) % 24 = y as both 0 <= x, y < 24.
        """
        res = 0
        cnt = [0] * 24
        for hour in hours:
            res += cnt[(24 - hour % 24) % 24]
            cnt[hour % 24] += 1
        return res

    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        nums = sorted(freq.keys())
        N = len(nums)

        @cache
        def dfs(i):
            if i >= N:
                return 0
            return max(
                dfs(i + 1),
                nums[i] * freq[nums[i]]
                + dfs(i + 1 + (nums[i] + 1 in freq) + (nums[i] + 2 in freq)),
            )

        return dfs(0)

    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        pass
