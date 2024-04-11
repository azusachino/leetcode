import sys
from typing import List
import heapq
from collections import Counter, deque


class PQItem:
    def __init__(self, priority: int, data: str):
        self.priority = priority
        self.data = data

    def __lt__(self, other) -> bool:
        return self.priority < other.priority

    def __repr__(self) -> str:
        return "%d @ %s" % (self.priority, self.data)


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(Counter(tasks).values())
        most_repeats = max(counts)
        num_longest = counts.count(most_repeats)
        return max(len(tasks), (most_repeats - 1) * (n + 1) + num_longest)

    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m, n = len(grid), len(grid[0])
        # -score, i,j
        pq = [(-grid[0][0], 0, 0)]
        seen = set((0, 0))
        res = sys.maxsize
        while True:
            score, x, y = heapq.heappop(pq)
            res = min(res, -score)
            if x == m - 1 and y == n - 1:
                return res
            for di, dj in dirs:
                i, j = di + x, dj + y
                if 0 <= i < m and 0 <= j < n and (i, j) not in seen:
                    heapq.heappush(pq, (-grid[i][j], i, j))
                    seen.add((i, j))


if __name__ == "__main__":
    solution = Solution()
    tasks = ["A", "A", "A", "B", "B", "B"]
    print("leastInterval", solution.leastInterval(tasks, 2))
    grid = [[5, 4, 5], [1, 2, 6], [7, 4, 6]]
    print(solution.maximumMinimumPath(grid))
