from typing import List


class Solution:
    """
    3280. Convert Date to Binary
        https://leetcode.com/problems/convert-date-to-binary/
    3281. Maximize Score of Numbers in Ranges
        https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/description/
    3282. Reach End of Array With Max Score
        https://leetcode.com/problems/reach-end-of-array-with-max-score/description/
    3283. Maximum Number of Moves to Kill All Pawns
        https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/description/
    """

    def convertDateToBinary(self, date: str) -> str:
        return "-".join(map(lambda x: str(bin(int(x)))[2:], date.split("-")))

    def maxPossibleScore(self, start: List[int], d: int) -> int:
        pass

    def findMaximumScore(self, nums: List[int]) -> int:
        pass

    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        pass
