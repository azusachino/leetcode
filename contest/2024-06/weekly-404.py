from itertools import groupby
from math import isqrt
from typing import List


class Solution:
    """
    3200. Maximum Height of a Triangle
        https://leetcode.com/problems/maximum-height-of-a-triangle/description/
    3201. Find the Maximum Length of Valid Subsequence I
        https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/
    3202. Find the Maximum Length of Valid Subsequence II
        https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/
    3203. Find Minimum Diameter After Merging Two Trees
        https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/description/
    """

    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        if red < blue:
            return self.maxHeightOfTriangle(blue, red)

        h1, h2 = isqrt(blue * 4 + 1), isqrt(blue) * 2
        if (h1 + 1) ** 2 // 4 <= red:
            return h1
        if ((h2 + 1) ** 2 - 1) // 4 <= red:
            return h2
        if (h1 - 1) ** 2 // 4 <= red:
            return h1 - 1
        return h2 - 1

    def maximumLength(self, A: List[int]) -> int:
        A = [a % 2 for a in A]
        # Grouping consecutive numbers
        return max(A.count(0), A.count(1), len(list(groupby(A))))

    def maximumLength(self, A: List[int], k: int) -> int:
        res = 0
        for v in range(k):
            dp = [0] * k
            for a in A:
                dp[a % k] = max(dp[a % k], dp[(v - a) % k] + 1)
            res = max(res, max(dp))
        return res

    # @credit lee215
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        def farthest(G, i):
            n = len(G)
            bfs = [i]
            seen = [0] * n
            seen[i] = 1
            res = maxd = -1
            for i in bfs:
                for j in G[i]:
                    if seen[j] == 0:
                        seen[j] = seen[i] + 1
                        bfs.append(j)
                        if seen[j] > maxd:
                            res = j
                            maxd = seen[j]
            return res, maxd - 1

        def diameter(edges):
            if not edges:
                return 0, 0, 0
            n = len(edges) + 1
            G = [[] for i in range(n)]
            for i, j in edges:
                G[i].append(j)
                G[j].append(i)
            v1, d = farthest(G, 0)
            v2, d = farthest(G, v1)
            return d, v1, v2

        d1, i, j = diameter(edges1)
        d2, i, j = diameter(edges2)
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)


if __name__ == "__main__":
    arr = [1, 2, 1, 1]
    a = [x % 2 for x in arr]
    print(len(list(groupby(a))))
