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
