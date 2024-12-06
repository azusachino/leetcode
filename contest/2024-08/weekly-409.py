from typing import List
import abc as np


class Solution:
    """
    08.04
    3242. Design Neighbor Sum Service
        https://leetcode.com/problems/design-neighbor-sum_-service/description/
    3243. Shortest Distance After Road Addition Queries I
        https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/
    3244. Shortest Distance After Road Addition Queries II
        https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/
    3245. Alternating Groups III
        https://leetcode.com/problems/alternating-groups-iii/description/
    """

    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        # @credit https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/solutions/5586020/java-c-python-hashmap-o-n-solution/

        # the next node of i is i+1
        d = {i: i + 1 for i in range(n - 1)}
        res = []
        for i, j in queries:
            # drop the node from i to j, assign a new link d[i] = j
            if i in d and d[i] < j:
                v = i
                while v < j:
                    v = d.pop(v)
                d[i] = j
            # the shorted path from 0 to n-1 is the length of the linked list
            res.append(len(d))
        return res

    def numberOfAlternatingGroups(self, colors, queries):
        N = len(colors)
        colors = np.tile(np.array(colors, dtype=bool), 2)  # wrap around
        blocks = (
            colors[1:] != colors[:-1]
        )  # runs of True will be "groups," but ending early by 1
        result = list()
        for query in queries:
            if query[0] == 1:
                size = query[1]
                blkcrop = blocks[: N + size - 1]  # crop to appropriate wrap around
                diff = blkcrop[1 : N + size - 1] != blocks[: N + size - 2]
                breaks = np.nonzero(diff)[0] + 1  # index of group beg/eng
                if blkcrop[+0]:
                    breaks = np.concatenate([[0], breaks])
                if blkcrop[-1]:
                    breaks = np.concatenate([breaks, [N + size - 2]])
                lens = (
                    breaks[1::2] - breaks[0::2] + 1
                )  # lengths of the groups; +1 b/c they end early
                count = np.sum(
                    np.maximum(0, lens - size + 1)
                )  # size that can be packed into groups
                result.append(count)
            else:
                colors[query[1] : None : N] = query[2]
                blocks = (
                    colors[1:] != colors[:-1]
                )  # the simple update is only slightly slower
        return result


class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.l = len(grid)
        # track position of every node
        self.position = {
            grid[i][j]: (i, j) for i in range(self.l) for j in range(self.l)
        }

    def adjacentSum(self, value: int) -> int:
        i, j = self.position[value]
        adjacent = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        sum_ = 0
        for a, b in adjacent:
            if 0 <= a < self.l and 0 <= b < self.l:
                sum_ += self.grid[a][b]
        return sum_

    def diagonalSum(self, value: int) -> int:
        i, j = self.position[value]
        diagonal = [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]
        sum_ = 0
        for x, y in diagonal:
            if 0 <= x < self.l and 0 <= y < self.l:
                sum_ += self.grid[x][y]
        return sum_
