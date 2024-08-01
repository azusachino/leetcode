import heapq
from itertools import accumulate
from typing import List


class Solution:
    """
    1640. Check Array Formation Through Concatenation
        https://leetcode.com/problems/check-array-formation-through-concatenation/description/
    1641. Count Sorted Vowel Strings
        https://leetcode.com/problems/count-sorted-vowel-strings/
    1642. Furthest Building You Can Reach
        https://leetcode.com/problems/furthest-building-you-can-reach/description/
    1643. Kth Smallest Instructions
        https://leetcode.com/problems/kth-smallest-instructions/description/
    """

    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        map_ = {x[0]: x for x in pieces}
        res = []

        for n in arr:
            res += map_.get(n, [])

        return res == arr

    def countVowelStrings(self, n: int) -> int:
        seen = {}

        # dp[n][k] means the number of strings constructed by at most k different characters.
        def dp(n, k):
            if k == 1 or n == 1:
                return k
            if (n, k) in seen:
                return seen[(n, k)]
            seen[(n, k)] = sum(dp(n - 1, k) for k in range(1, k + 1))
            return seen[(n, k)]

        return dp(n, 5)

    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        for i in range(n):
            dp = accumulate(dp)
        return list(dp)[-1]

    def countVowelStrings(self, n: int) -> int:
        return (n + 1) * (n + 2) * (n + 3) * (n + 4) // 24

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        n = len(heights)
        for i in range(n - 1):
            d = heights[i + 1] - heights[i]
            if d > 0:
                # pretend we are using ladders greedily
                heapq.heappush(pq, d)
            # no ladders left
            if len(pq) > ladders:
                bricks -= heapq.heappop(pq)
            # no bricks left
            if bricks < 0:
                return i
        return n - 1

    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        from math import comb

        r, c = destination

        ret = []
        remDown = r
        for i in range(r + c):
            remSteps = r + c - (i + 1)
            com = comb(remSteps, remDown)
            if com >= k:
                ret.append("H")
            else:
                remDown -= 1
                k -= com
                ret.append("V")

        return "".join(ret)
