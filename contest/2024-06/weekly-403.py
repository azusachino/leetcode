import sys
from typing import List


class Solution:
    """
    2024.06.23
    3194. Minimum Average of Smallest and Largest Elements
        https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/description/
    3195. Find the Minimum Area to Cover All Ones I
        https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/description/
    3196. Maximize Total Cost of Alternating Subarrays
        https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/description/
    3197. Find the Minimum Area to Cover All Ones II
        https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/description/
    """

    def minimumAverage(self, nums: List[int]) -> float:
        ns = []
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            ns.append((nums[i] + nums[j]) / 2)
            i += 1
            j -= 1
        return min(ns)

    def minimumArea(self, grid: List[List[int]]) -> int:
        """
        Find Boundaries:  Iterate through the grid and find the topmost (top), bottommost (bottom), leftmost (left), and rightmost (right) rows and columns containing 1s. These boundaries define the smallest possible rectangle that could enclose all 1s.

        Check Validity:  If any of the boundaries are missing (i.e., no 1s in a certain direction), return 0 (no solution possible).

        Calculate Area: The area of the rectangle is simply (bottom - top + 1) * (right - left + 1). Return this value.
        """
        top, bottom, left, right = sys.maxsize, -1, sys.maxsize, -1
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    top = min(top, i)
                    bottom = max(bottom, i)
                    left = min(left, j)
                    right = max(right, j)

        if top <= bottom and left <= right:
            return (bottom - top + 1) * (right - left + 1)
        return 0

    def maximumTotalCost(self, nums):
        add_result = nums[0]
        sub_result = nums[0]

        for i in range(1, len(nums)):
            temp_add = max(add_result, sub_result) + nums[i]
            temp_sub = add_result - nums[i]

            add_result = temp_add
            sub_result = temp_sub

        return max(add_result, sub_result)
