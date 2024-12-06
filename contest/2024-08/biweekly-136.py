from typing import Counter, List


class Solution:
    """
    08.04
    3238. Find the Number of Winning Players
        https://leetcode.com/problems/find-the-number-of-winning-players/description/
    3239. Minimum Number of Flips to Make Binary Grid Palindromic I
        https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/description/
    3240. Minimum Number of Flips to Make Binary Grid Palindromic II (10*5)
        https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/description/
    3241. Time Taken to Mark All Nodes
        https://leetcode.com/problems/time-taken-to-mark-all-nodes/description/
    """

    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        ctr = Counter(map(tuple, pick))
        return len({player for (player, _), count in ctr.items() if count > player})

    def minFlips(self, grid: List[List[int]]) -> int:
        # all rows or all columns
        r, c = len(grid), len(grid[0])
        rc, cc = 0, 0
        for i in range(r):
            for j in range(c // 2):
                if grid[i][j] != grid[i][c - j - 1]:
                    rc += 1
        for i in range(c):
            for j in range(r // 2):
                if grid[j][i] != grid[r - j - 1][i]:
                    cc += 1
        return min(rc, cc)

    def minFlips(self, A: List[List[int]]) -> int:
        # all rows and columns
        # @credit https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/solutions/5585642/java-c-python-symmetry/
        res = one = diff = 0
        m, n = len(A), len(A[0])
        for i in range(m // 2):
            for j in range(n // 2):
                v = A[i][j] + A[i][~j] + A[~i][j] + A[~i][~j]
                res += min(v, 4 - v)
        if n % 2:
            for i in range(m // 2):
                diff += A[i][n // 2] ^ A[~i][n // 2]
                one += A[i][n // 2] + A[~i][n // 2]
        if m % 2:
            for j in range(n // 2):
                diff += A[m // 2][j] ^ A[m // 2][~j]
                one += A[m // 2][j] + A[m // 2][~j]
        if n % 2 and m % 2:
            res += A[m // 2][n // 2]
        if diff == 0 and one % 4:
            res += 2
        return res + diff

    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        pass
