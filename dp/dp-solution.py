from collections import defaultdict
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

    def longestStrChain(self, words: List[str]) -> int:
        table = defaultdict(set)
        # length -> word set
        for w in words:
            table[len(w)].add(w)

        dp = defaultdict(lambda: 1)
        # problem constraint, only 16-len words permitted
        ## start from 2, bottom to top dp
        for k in range(2, 17):
            for w in table[k]:
                # try to delete each index
                for i in range(k):
                    prev_word = w[:k] + w[k + 1 :]
                    if prev_word in table[k - 1]:
                        dp[w] = max(dp[w], dp[prev_word] + 1)

        return max(dp.values() or [1])

    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        If x in the set dp, it means the difference x is achievable currently.
        """
        dp = {0}
        for s in stones:
            dp = {s + i for i in dp} | {abs(s - i) for i in dp}
        return min(dp)
