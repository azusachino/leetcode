from collections import defaultdict, deque
from functools import cache
from math import inf
from typing import Counter, List, Tuple


class Solution:
    """
    1128. Number of Equivalent Domino Pairs
        https://leetcode.ca/2019-01-01-1128-Number-of-Equivalent-Domino-Pairs/
    1129. Shortest Path with Alternating Colors
        https://leetcode.ca/2019-01-02-1129-Shortest-Path-with-Alternating-Colors/
    1130. Minimum Cost Tree From Leaf Values
        https://leetcode.ca/2019-01-03-1130-Minimum-Cost-Tree-From-Leaf-Values/
        https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/solutions/339959/one-pass-o-n-time-and-space/
    1131. Maximum of Absolute Value Expression
        https://leetcode.ca/2019-01-04-1131-Maximum-of-Absolute-Value-Expression/
    """

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = Counter()
        res = 0
        for x, y in dominoes:
            # skip the first one (as pair count)
            res += count[(x, y)]
            count[(x, y)] += 1
            # the counterpart pair
            if x != y:
                count[(y, x)] += 1
        return res

    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        g = [defaultdict(list), defaultdict(list)]
        # adj table for red/blue, directed vector
        for i, j in redEdges:
            g[0][i].append(j)
        for i, j in blueEdges:
            g[1][i].append(j)

        res = [-1] * n
        seen = set()
        step = 0
        # from index 0, go to red or blue edge (index, color)
        q = deque([(0, 0), (0, 1)])
        while q:
            sz = len(q)
            for _ in range(sz):
                i, c = q.popleft()
                # already reach the index, update with the least step
                if res[i] == -1:
                    res[i] = step
                seen.add((i, c))
                # swith color
                c ^= 1
                for j in g[c][i]:
                    if (j, c) not in seen:
                        q.append((j, c))
            step += 1
        return res

    def mctFromLeafValues(self, arr: List[int]) -> int:
        @cache
        def dfs(i: int, j: int) -> Tuple:
            if i == j:
                return 0, arr[i]
            s, mx = inf, -1
            for k in range(i, j):
                s1, mx1 = dfs(i, k)
                s2, mx2 = dfs(k + 1, j)
                t = s1 + s2 + mx1 * mx2
                if s > t:
                    s = t
                    mx = max(mx1, mx2)
            return s, mx

        return dfs(0, len(arr) - 1)[0]

    def mctFromLeafValues_(self, A):
        res = 0
        stack = [float("inf")]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res

    def maxAbsValExpr(self, x: List[int], y: List[int]) -> int:
        res = 0
        n = len(x)
        dirs = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
        for p, q in dirs:
            smallest = p * x[0] + q * y[0] + 0
            for i in range(n):
                cur = p * x[i] + q * y[i] + i
                res = max(res, cur - smallest)
                smallest = min(smallest, cur)
        return res
