from itertools import accumulate
from typing import List


class Solution:
    """
    1688. Count of Matches in Tournament
        https://leetcode.com/problems/count-of-matches-in-tournament/description/
    1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
        https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/
    1690. Stone Game VII
        https://leetcode.com/problems/stone-game-vii/description/
    1691. Maximum Height by Stacking Cuboids
        https://leetcode.com/problems/maximum-height-by-stacking-cuboids/description/
    """

    def numberOfMatches(self, n: int) -> int:
        # The champion never lose, n - 1 other teams lose.
        return n - 1

    def minPartitions(self, n: str) -> int:
        # @credit https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/solutions/970318/java-c-python-just-return-max-digit/
        return int(max(n))

    def stoneGameVII(self, s: List[int]) -> int:
        # @credit https://leetcode.com/problems/stone-game-vii/solutions/970268/c-python-o-n-n/
        dp = [[0] * len(s) for _ in range(len(s))]
        p_sum = [0] + list(accumulate(s))
        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                dp[i][j] = max(
                    p_sum[j + 1] - p_sum[i + 1] - dp[i + 1][j],
                    p_sum[j] - p_sum[i] - dp[i][j - 1],
                )
        return dp[0][len(s) - 1]

    def maxHeight(self, A):
        # @credit https://leetcode.com/problems/maximum-height-by-stacking-cuboids/solutions/970293/java-c-python-dp-prove-with-explanation/
        A = [[0, 0, 0]] + sorted(map(sorted, A))
        dp = [0] * len(A)
        for j in range(1, len(A)):
            for i in range(j):
                if all(A[i][k] <= A[j][k] for k in range(3)):
                    dp[j] = max(dp[j], dp[i] + A[j][2])
        return max(dp)
