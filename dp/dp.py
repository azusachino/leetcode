from typing import List
import sys


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        dp = [sys.maxsize] * n
        dp[src] = 0

        def helper() -> bool:
            current = dp[:]
            result = True
            # to find feasible start_point, add up prices
            for x, y, z in flights:
                # return True when dp[dst] first equals price[start] + price (accumulated price)
                if current[x] < sys.maxsize and dp[y] > dp[x] + z:
                    dp[y] = z + current[x]
                    result = False
            return result

        for _ in range(k + 1):
            if helper():
                break
        if dp[dst] == sys.maxsize:
            return -1
        else:
            return dp[dst]
