from typing import List


class Solution:
    """
    3274. Check if Two Chessboard Squares Have the Same Color
        https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/description/
    3275. K-th Nearest Obstacle Queries
        https://leetcode.com/problems/k-th-nearest-obstacle-queries/
    3276. Select Cells in Grid With Maximum Score
        https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/description/
    3277. Maximum XOR Score Subarray Queries
        https://leetcode.com/problems/maximum-xor-score-subarray-queries/description/
    """

    def checkTwoChessboards(self, A: str, B: str) -> bool:
        a, b = list(A)
        c, d = list(B)
        x, y = abs(ord(c) - ord(a)), abs(int(d) - int(b))
        return max(x, y) % 2 == min(x, y) % 2

    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        pass

    def maxScore(self, grid: List[List[int]]) -> int:
        pass

    def maximumSubarrayXor(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        pass
