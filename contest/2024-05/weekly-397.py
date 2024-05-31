from math import inf
from typing import List


class Solution:
    """
    3146. Permutation Difference between Two Strings
        https://leetcode.com/problems/permutation-difference-between-two-strings/description/
        string, permutation
    3147. Taking Maximum Energy From the Mystic Dungeon
        https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/description/
        array
    3148. Maximum Difference Score in a Grid
        https://leetcode.com/problems/maximum-difference-score-in-a-grid/description/
        graph
    3149. Find the Minimum Cost Array Permutation
        https://leetcode.com/problems/find-the-minimum-cost-array-permutation/description/
        DP, bitmask
    """

    def findPermutationDifference(self, s: str, t: str) -> int:
        def helper(s):
            v = {}
            for i, c in enumerate(s):
                # only occur once
                v[c] = i
            return v

        x, y = helper(s), helper(t)
        res = 0
        for c in s:
            res += abs(x[c] - y[c])
        return res

    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)

        for j in range(n - k - 1, -1, -1):
            energy[j] += energy[j + k]

        return max(energy)

    def maxScore(self, A: List[List[int]]) -> int:
        res, m, n = -inf, len(A), len(A[0])
        for i in range(m):
            for j in range(n):
                pre = min(A[i-1][j] if i else inf, A[i][j-1] if j else inf)
                res = max(res, A[i][j] - pre)
                A[i][j] = min(A[i][j], pre)
        return res


    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [[[-1, 1e9] for i in range(1<<(n-1))] for j in range((n - 1))]
        for i in range(n-1): # take i + 1
            dp[i][1<<i] = [-1, abs(i+1-nums[0])]
        for k in range(1 << (n-1)):
            for j in range(n-1):
                if k & (1<<j):
                    for i in range(n-1):
                        if i == j:
                            continue
                        if k & (1<<i):
                            if dp[i][k ^ (1<<j)][1] + abs(j + 1 - nums[i+1]) < dp[j][k][1]:
                                dp[j][k] = [i, dp[i][k ^ (1<<j)][1] + abs(j+1 - nums[i+1])]
        st = -1
        stsc = 1e9
        for i in range(n-1):
            if dp[i][-1][1] + abs(-nums[i+1]) < stsc:
                st = i
                stsc = dp[i][(1<<(n-1)) - 1][1] + abs(-nums[i+1])
        ans = [0]
        pre = st
        nowmask = (1<<(n-1)) - 1
        while pre != -1:
            ans.append(pre+1)
            p = pre
            pre = dp[pre][nowmask][0]
            nowmask ^= 1<<p
        return ans