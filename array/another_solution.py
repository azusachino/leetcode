import collections
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        result = cur = 0
        d = collections.deque(sorted(tokens))
        while d and (d[0] <= power or cur):
            if d[0] <= power:
                power -= d.popleft()
                cur += 1
            else:
                power += d.pop()
                cur -= 1
            result = max(result, cur)
        return result

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        highest = 0
        ret = 0
        for i in range(n - 1, -1, -1):
            ret = max(ret, highest - prices[i])
            highest = max(highest, prices[i])
        return ret

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        TLE
        """
        n = len(nums)
        cnt = 0
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                if cur == goal:
                    cnt += 1
                elif cur > goal:
                    break

        return cnt

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [1] * n
        cur = 1
        for i in range(n):
            ret[i] *= cur
            cur *= nums[i]
        cur = 1
        for i in range(n - 1, -1, -1):
            ret[i] *= cur
            cur *= nums[i]
        return ret
