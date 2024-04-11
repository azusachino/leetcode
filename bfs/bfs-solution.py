from collections import defaultdict, deque
import collections
from itertools import groupby
from typing import List


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        can = {0, firstPerson}
        for _, grp in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            queue = set()
            graph = defaultdict(list)
            for x, y, _ in grp:
                graph[x].append(y)
                graph[y].append(x)
                if x in can:
                    queue.add(x)
                if y in can:
                    queue.add(y)

            queue = deque(queue)
            while queue:
                x = queue.popleft()
                for y in graph[x]:
                    if y not in can:
                        can.add(y)
                        queue.append(y)
        return can

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # square
        n = len(grid)
        # check start/end validity
        if grid[0][0] or grid[-1][-1]:
            return -1

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [1, -1], [-1, 1]]

        seen = {(0, 0)}
        queue = collections.deque((0, 0, 1))
        while queue:
            i, j, d = queue.popleft()
            if i == n - 1 and j == n - 1:
                return d
            for di, dj in dirs:
                x, y = di + i, dj + j
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0 and (x, y) not in seen:
                    seen.add((x, y))
                    queue.append((x, y, d + 1))
        return -1
