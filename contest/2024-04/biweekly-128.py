from collections import defaultdict
import heapq
from itertools import pairwise
import sys
from typing import List


class Solution:
    """
    3110. Score of a String
    3111. Minimum Rectangles to Cover Points
    3112. Minimum Time to Visit Disappearing Nodes
    3113. Find the Number of Subarrays Where Boundary Elements Are Maximum
    """

    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(x) - ord(y)) for x, y in pairwise(s))

    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        res = 0
        last = -1
        for x, _ in sorted(points):
            if x > last:
                res += 1
                last = x + w
        return res

    def minimumTime(
        self, n: int, edges: List[List[int]], disappear: List[int]
    ) -> List[int]:
        adj = defaultdict(list)
        for u, v, l in edges:
            adj[u].append((l, v))
            adj[v].append((l, u))

        # index, time-used
        pq = [(0, 0)]

        res = [sys.maxsize] * n
        res[0] = 0

        while pq:
            time, index = heapq.heappop(pq)
            # not accessed or a fast route
            if time > res[index]:
                continue

            # print(index, time, disappear[index], pq)
            # this node already disappered
            for v, j in adj[index]:
                new_time = time + v
                if new_time < disappear[j] and new_time < res[j]:
                    res[j] = new_time
                    heapq.heappush(pq, (new_time, j))

        for i in range(n):
            if res[i] == sys.maxsize:
                res[i] = -1

        return res

    def numberOfSubarrays(self, nums: List[int]) -> int:
        """
        Each element in the stack holds:
            The value of the element itself.
            The count of subarrays where this element is the minimum thus far.

        For each a in A, we try to find the subarray ending at a.
        firstly pop all element smaller than a,
        This ensures that the stack maintains monotonically decreasing.

        If stack doesn't end, we push a to the stack.
        then we update the occurence of a, finally increment the occurence to result res.
        """
        stk = []
        res = 0
        for n in nums:
            # pop out the smaller ones, as they are not qualified as maximum
            while stk and stk[-1][0] < n:
                stk.pop()
            # append smaller ones with weight 0, as they might be maximum
            if not stk or stk[-1][0] > n:
                stk.append([n, 0])
            # same weight e.g. [1,4,3,3,2] -> [[4, 1], [3, 2], [2, 1]]
            stk[-1][1] += 1
            # how many subarray can form if current num as maximum
            res += stk[-1][1]
        return res


if __name__ == "__main__":
    solution = Solution()
    edges = [
        [7, 0, 10],
        [0, 1, 4],
        [8, 8, 4],
        [1, 6, 1],
        [1, 0, 7],
        [8, 4, 9],
        [1, 7, 1],
        [1, 0, 10],
    ]
    disappear = [6, 15, 20, 10, 7, 11, 5, 14, 13]
    # print(solution.minimumTime(9, edges, disappear))
    points = [[2, 1], [1, 0], [1, 4], [1, 8], [3, 5], [4, 6]]
    print(solution.minRectanglesToCoverPoints(points, 1))
