import heapq
import sys
from typing import Counter, List


class UF:
    def __init__(self, n: int):
        self.data = list(range(n))
        self.rank = [1] * n
        self.cnt = n

    def find(self, x):
        if self.data[x] != x:
            self.data[x] = self.find(self.data[x])
        return self.data[x]

    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a != b:
            if self.rank[a] >= self.rank[b]:
                self.data[b] = a
                self.rank[a] += self.rank[b]
            else:
                self.data[a] = b
                self.rank[b] += self.rank[a]
            self.cnt -= 1

    def count(self):
        return self.cnt


class Solution:
    """
    1099. Two Sum Less Than K
    1100.1 Find K-Length Substrings With No Repeated Characters
    1100.2 Find Substrings With No Repeated Characters
    1101. The Earliest Moment When Everyone Become Friends
    1102. Path With Maximum Minimum Value
    """

    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        """
        Input: s = "havefunonleetcode", k = 5
        Output: 6
        Input: s = "home", k = 5
        Output: 0
        """
        n = len(s)
        # impossible to construct distinct characters beyond
        if k > 26 or k > n:
            return 0
        count = Counter()
        l = res = 0
        for r in range(n):
            count[s[r]] += 1
            # when s[r] is not distinct or the range is larger
            while count[s[r]] > 1 or r - l + 1 > k:
                count[s[l]] -= 1
                l += 1
            res += r - l + 1 == k
        return res

    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        """
        Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
        Output: 20190301
        """
        uf = UF(n)
        # sort, to find the first index
        logs.sort()
        for t, x, y in logs:
            uf.union(x, y)
            if uf.count() == 1:
                return t
        return -1

    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        """
        Input: grid = [[5,4,5],[1,2,6],[7,4,6]]
        Output: 4
        Input: grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
        Output: 2
        Input: grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
        Output: 3
        """
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m, n = len(grid), len(grid[0])
        # use priority_queue to select possible maximum path greedily (negative as largest (min_heap))
        pq = [(-grid[0][0], 0, 0)]
        # visited set
        seen = set((0, 0))
        # worse case?
        min_val = sys.maxsize
        while True:
            score, x, y = heapq.heappop(pq)
            # track the minimum value
            min_val = min(min_val, -score)
            if x == m - 1 and y == n - 1:
                return min_val
            # bfs
            for di, dj in dirs:
                i, j = x + di, y + dj
                if 0 <= i < m and 0 <= j < n and (i, j) not in seen:
                    heapq.heappush(pq, (-grid[i][j], i, j))
                    seen.add((i, j))


class Solution2:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        """
        Input: s = "havefunonleetcode", k = 5
        Output: 6
        Input: s = "home", k = 5
        Output: 0
        """
        n = len(s)
        # impossible to construct distinct characters beyond
        if k > 26 or k > n:
            return 0

        res = 0

        for i in range(n - k + 1):
            if len(set(s[i : i + k])) == len(s[i : i + k]):
                res += 1
        return res


if __name__ == "__main__":
    solution = Solution()
    s = "havefunonleetcode"
    print(solution.numKLenSubstrNoRepeats(s, 5))
    logs = [
        [20190101, 0, 1],
        [20190104, 3, 4],
        [20190107, 2, 3],
        [20190211, 1, 5],
        [20190224, 2, 4],
        [20190301, 0, 3],
        [20190312, 1, 2],
        [20190322, 4, 5],
    ]
    print(solution.earliestAcq(logs, 6))
    grid = [[5, 4, 5], [1, 2, 6], [7, 4, 6]]
    print(solution.maximumMinimumPath(grid))
