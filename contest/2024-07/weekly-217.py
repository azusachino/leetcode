import collections
import heapq
import math
from typing import List


class Solution:
    """
    1672. Richest Customer Wealth
        https://leetcode.com/problems/richest-customer-wealth/description/
    1673. Find the Most Competitive Subsequence
        https://leetcode.com/problems/find-the-most-competitive-subsequence/description/
    1674. Minimum Moves to Make Array Complementary
        https://leetcode.com/problems/minimum-moves-to-make-array-complementary/description/
    1675. Minimize Deviation in Array
        https://leetcode.com/problems/minimize-deviation-in-array/description/
    """

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(x) for x in accounts])

    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """
        monotonic stack
        for ensuring stk length, before popping out, check its length with current index
        """
        stk = []
        n = len(nums)
        for i, v in enumerate(nums):
            # find a smaller one, and the rest elements are more than k
            while stk and stk[-1] > v and len(stk) + n - i > k:
                stk.pop()
            if len(stk) < k:
                stk.append(v)
        return stk

    def minMoves(self, nums: List[int], limit: int) -> int:
        # @credit https://leetcode.com/problems/minimum-moves-to-make-array-complementary/solutions/952773/python-java-simple-o-max-n-k-method/
        delta = collections.Counter()
        n = len(nums)
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            delta[2] += 2
            delta[min(a, b) + 1] -= 1
            delta[a + b] -= 1
            delta[a + b + 1] += 1
            delta[max(a, b) + limit + 1] += 1

        curr = 0
        res = math.inf
        for i in range(2, 2 * limit + 1):
            curr += delta[i]
            res = min(res, curr)
        return res

    def minimumDeviation(self, nums: List[int]) -> int:
        pq = [-num * 2 if num % 2 == 1 else -num for num in nums]
        heapq.heapify(pq)
        min_val = -float("inf")
        for num in nums:
            min_val = min(min_val, -num if num % 2 == 0 else -num * 2)
        min_deviation = float("inf")
        while True:
            max_val = -heapq.heappop(pq)
            min_deviation = min(min_deviation, max_val - min_val)
            if max_val % 2 == 1:
                break
            max_val //= 2
            min_val = min(min_val, -max_val)
            heapq.heappush(pq, -max_val)
        return min_deviation
