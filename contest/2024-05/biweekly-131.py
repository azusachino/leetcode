from typing import Counter, List


class Solution:
    """
    3158. Find the XOR of Numbers Which Appear Twice
        https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/
    """

    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = 0
        for x, y in freq.items():
            if y == 2:
                res ^= x
        return res
