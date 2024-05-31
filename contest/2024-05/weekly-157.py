from collections import defaultdict
from itertools import pairwise
from typing import List


class Solution:
    """
    1217. Minimum Cost to Move Chips to The Same Position
        https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/description/
        array
    1218. Longest Arithmetic Subsequence of Given Difference
        https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/
        array, dp
    1219. Path with Maximum Gold
        https://leetcode.com/problems/path-with-maximum-gold/description/
        graph, dfs
    1220. Count Vowels Permutation
        https://leetcode.com/problems/count-vowels-permutation/
        string (vowel), DP
    """

    def minCostToMoveChips(self, position: List[int]) -> int:
        a = sum(p % 2 for p in position)
        b = len(position) - a
        return min(a, b)

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        f = defaultdict(int)
        for x in arr:
            f[x] = f[x - difference] + 1
        return max(f.values())

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            if not (0 <= i < m and 0 <= j < n and grid[i][j]):
                return 0
            v = grid[i][j]
            grid[i][j] = 0
            ans = max(dfs(i + a, j + b) for a, b in pairwise(dirs)) + v
            grid[i][j] = v
            return ans

        m, n = len(grid), len(grid[0])
        dirs = (-1, 0, 1, 0, -1)
        return max(dfs(i, j) for i in range(m) for j in range(n))

    def countVowelPermutation(self, n: int) -> int:
        f = [1] * 5
        mod = 10**9 + 7
        for _ in range(n - 1):
            g = [0] * 5
            g[0] = (f[1] + f[2] + f[4]) % mod
            g[1] = (f[0] + f[2]) % mod
            g[2] = (f[1] + f[3]) % mod
            g[3] = f[2]
            g[4] = (f[2] + f[3]) % mod
            f = g
        return sum(f) % mod
