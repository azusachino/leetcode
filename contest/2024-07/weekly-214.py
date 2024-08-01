from collections import Counter
import heapq
from typing import List


class Solution:
    """
    1646. Get Maximum in Generated Array
        https://leetcode.com/problems/get-maximum-in-generated-array/description/
    1647. Minimum Deletions to Make Character Frequencies Unique
        https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
    1648. Sell Diminishing-Valued Colored Balls
        https://leetcode.com/problems/sell-diminishing-valued-colored-balls/description/
    1649. Create Sorted Array through Instructions
        https://leetcode.com/problems/create-sorted-array-through-instructions/description/
    """

    def getMaximumGenerated(self, n: int) -> int:
        dp = [0] * (n + 2)
        dp[1] = 1
        for i in range(1, n // 2 + 1):
            dp[i * 2] = dp[i]
            dp[i * 2 + 1] = dp[i] + dp[i + 1]
        return max(dp[: n + 1])

    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        used = set()
        res = 0
        for freq in cnt.values():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        return res

    def maxProfit(self, inventory: List[int], orders: int) -> int:
        """
        only works under simple cases
        """
        pq = []
        for iv in inventory:
            heapq.heappush(pq, -iv)
        res = 0
        while orders:
            v = heapq.heappop(pq)
            res -= v
            heapq.heappush(pq, v + 1)
            orders -= 1
        return res

    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7
        sorted_inventory = sorted(inventory, reverse=True) + [0]
        max_profit = i = 0
        width = 1

        while orders:
            units_taken = min(
                orders, width * (sorted_inventory[i] - sorted_inventory[i + 1])
            )
            whole, remainder = divmod(units_taken, width)
            max_profit += width * self.get_sum(
                sorted_inventory[i] - whole + 1, sorted_inventory[i]
            )
            max_profit += remainder * (sorted_inventory[i] - whole)
            i += 1
            width += 1
            orders -= units_taken

        return max_profit % MOD

    def get_sum(self, a: int, b: int) -> int:
        return ((b - a + 1) * (a + b)) // 2

    def createSortedArray(self, instructions: List[int]) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()
    inv = [100000]
    orders = 1000000
    print(solution.maxProfit(inv, orders))
