import collections
import heapq
from typing import Counter, List


class Solution:
    """
    2024.07.06
    3206. Alternating Groups I
        https://leetcode.com/problems/alternating-groups-i/description/


    3208. Alternating Groups II
        https://leetcode.com/problems/alternating-groups-ii/description/
    3209. Number of Subarrays With AND Value of K
        https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/description/
    """

    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        res = 0
        colors += colors
        for i in range(n):
            if colors[i] == colors[i + 2] and colors[i] != colors[i + 1]:
                res += 1
        return res

    def maximumPoints(self, enemyEnergies, currentEnergy):
        profit = 0
        enemyEnergies.sort()
        n = len(enemyEnergies)

        if enemyEnergies[0] > currentEnergy:
            return 0

        j = n - 1
        while j >= 0:
            if enemyEnergies[0] <= currentEnergy:
                profit += currentEnergy // enemyEnergies[0]
                currentEnergy %= enemyEnergies[0]
            else:
                currentEnergy += enemyEnergies[j]
                j -= 1

        return profit

    def numberOfAlternatingGroups2(self, colors: List[int], k: int) -> int:
        colors += colors[: k - 1]
        res = 0
        cnt = 1
        for i in range(1, len(colors)):
            if colors[i] != colors[i - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                res += 1
        return res

    def countSubarrays(self, nums: List[int], k: int) -> int:
        cnt, res = Counter(), 0
        for n in nums:
            cnt1 = Counter()
            if k & n == k:
                cnt[n] += 1
                for v, count in cnt.items():
                    cnt1[v & n] += count
                res += cnt1[k]
            cnt = cnt1
        return res
