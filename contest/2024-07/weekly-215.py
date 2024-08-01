from functools import lru_cache
import sys
from typing import Counter, List


class Solution:
    """
    1656. Design an Ordered Stream
        https://leetcode.com/problems/design-an-ordered-stream/description/
    1657. Determine if Two Strings Are Close
        https://leetcode.com/problems/determine-if-two-strings-are-close/description/
    1658. Minimum Operations to Reduce X to Zero
        https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/
    1659. Maximize Grid Happiness
        https://leetcode.com/problems/maximize-grid-happiness/description/
    """

    def closeStrings(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        return sorted(c2.values()) == sorted(c1.values()) and c1.keys() == c2.keys()

    def minOperations(self, nums: List[int], x: int) -> int:
        """
        Find the Longest Subarray with Sum Equals to TotalSum - X
        """
        n = len(nums)
        target = sum(nums) - x
        if target == 0:
            return n

        res = -sys.maxsize
        cur_sum = 0
        d = {0: -1}
        for i in range(n):
            cur_sum += nums[i]
            # [1,1,4,2,3] 5 -> 6 6 3 -> 2
            if cur_sum - target in d:
                res = max(res, d[cur_sum - target])
            d[cur_sum] = i
        return -1 if res == -sys.maxsize else n - res

    def getMaxGridHappiness(self, m, n, I, E):
        InG, ExG, InL, ExL = 120, 40, -30, 20
        fine = [[0, 0, 0], [0, 2 * InL, InL + ExL], [0, InL + ExL, 2 * ExL]]

        @lru_cache(None)
        def dp(index, row, I, E):
            if index == -1:
                return 0

            R, C, ans = index // n, index % n, []
            neibs = [(1, I - 1, E, InG), (2, I, E - 1, ExG), (0, I, E, 0)]

            for val, dx, dy, gain in neibs:
                tmp = 0
                if dx >= 0 and dy >= 0:
                    tmp = dp(index - 1, (val,) + row[:-1], dx, dy) + gain
                    if C < n - 1:
                        tmp += fine[val][row[0]]  # right neighbor
                    if R < m - 1:
                        tmp += fine[val][row[-1]]  # down neighbor
                ans.append(tmp)

            return max(ans)

        if m < n:
            m, n = n, m

        return dp(m * n - 1, tuple([0] * n), I, E)


class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        res = []

        if idKey == self.ptr:
            while self.ptr < len(self.stream) and self.stream[self.ptr]:
                res.append(self.stream[self.ptr])
                self.ptr += 1
        return res
