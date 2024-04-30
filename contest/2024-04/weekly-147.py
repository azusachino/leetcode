from functools import cache
from itertools import accumulate
from typing import List


class Solution:
    """
    1137. N-th Tribonacci Number
        dp / O(1) memory / recursive with cache
    1138. Alphabet Board Path
    1139. Largest 1-Bordered Square
        https://leetcode.ca/2019-01-12-1139-Largest-1-Bordered-Square/
    1140. Stone Game II
    """

    def tribonacci(self, n: int) -> int:
        # initialize with 1,0,0, so we could iterate from 0
        a, b, c = 1, 0, 0
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return c

    def alphabetBoardPath(self, target: str) -> str:
        """
        Calculate this difference of coordinates.

        Notice that moving down and moving right,
        may move into a square that doesn't exist.
        To avoid this, we put L U before R D. (edge case of 'z')
        """
        # the representative of board
        d = {c: [i // 5, i % 5] for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        i, j = 0, 0
        res = []
        for c in target:
            x, y = d[c]
            if y < j:
                res.append("L" * (j - y))
            if x < i:
                res.append("U" * (i - x))
            if x > i:
                res.append("D" * (x - i))
            if y > j:
                res.append("R" * (y - j))
            # we reached the target c
            res.append("!")
            i, j = x, y
        return "".join(res)

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        """
        Count the number of consecutive 1s on the top and on the left.
        From length of edge l = min(m,n) to l = 1, check if the 1-bordered square exist.
        """
        m, n = len(grid), len(grid[0])
        down = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    down[i][j] = down[i + 1][j] + 1 if i + 1 < m else 1
                    right[i][j] = right[i][j + 1] + 1 if j + 1 < n else 1
        for k in range(min(m, n), 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if (
                        down[i][j] >= k
                        and right[i][j] >= k
                        and right[i + k - 1][j] >= k
                        and down[i][j + k - 1] >= k
                    ):
                        return k * k
        return 0

    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def dfs(i, m):
            if m * 2 >= n - i:
                return s[n] - s[i]
            return max(
                s[n] - s[i] - dfs(i + x, max(m, x)) for x in range(1, m << 1 | 1)
            )

        n = len(piles)
        s = list(accumulate(piles, initial=0))
        return dfs(0, 1)
