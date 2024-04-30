from functools import cache
import heapq
import sys
from typing import List


class Solution:
    """
    3120. Count the Number of Special Characters I
        string, count
    3121. Count the Number of Special Characters II
        string, count, order
    3122. Minimum Number of Operations to Satisfy Conditions
        dp
    3123. Find Edges in Shortest Paths
        Dijkstra
    """

    def numberOfSpecialChars(self, word: str) -> int:
        lower = upper = 0
        for ch in word:
            if ch.islower():
                lower |= 1 << ord(ch) - 97
            else:
                upper |= 1 << ord(ch) - 65
        return (lower & upper).bit_count()

    def numberOfSpecialChars_(self, word: str) -> int:
        lo, up = [False] * 26, [False] * 26
        for ch in word:
            if ch.islower():
                lo[ord(ch) - ord("a")] = not up[ord(ch) - ord("a")]
            else:
                up[ord(ch) - ord("A")] = True
        return sum([a and b for a, b in zip(lo, up)])

    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # count the number of each column
        count = [[0 for _ in range(10)] for _ in range(n)]

        for i in range(m):
            for j in range(n):
                count[j][grid[i][j]] += 1

        # dp(j, prv): the minimun changes at column j and the right column value is prv
        @cache
        def dp(j, prv_value):
            # if we reach the last column, return 0 as we do not need to pick value.
            if j == -1:
                return 0

            result = sys.maxsize
            # iterate all 10 values
            for val in range(10):
                # can't choose the same value as right hand
                if val != prv_value:
                    # column j has 'count[j][val]' val, so we need to change the remaining values to val, m - count[j][val]
                    result = min(result, m - count[j][val] + dp(j - 1, val))
            return result

        return dp(n - 1, -1)

    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def fn(source):
            dist = [sys.maxsize] * n
            dist[source] = 0
            pq = [(0, source)]
            while pq:
                x, u = heapq.heappop(pq)
                if dist[u] == x:
                    for v, w in graph[u]:
                        if x + w < dist[v]:
                            dist[v] = x + w
                            heapq.heappush(pq, (x + w, v))
            return dist

        dist0, dist1 = fn(0), fn(n - 1)
        return [
            dist0[n - 1] < sys.maxsize
            and (
                dist0[u] + w + dist1[v] == dist0[n - 1]
                or dist0[v] + w + dist1[u] == dist0[n - 1]
            )
            for u, v, w in edges
        ]
