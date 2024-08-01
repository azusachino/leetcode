from math import comb
from typing import List


class Solution:
    """
    2024.06.09
    3178. Find the Child Who Has the Ball After K Seconds
        https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/description/
    3179. Find the N-th Value After K Seconds
        https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/
    3180. Maximum Total Reward Using Operations I
        https://leetcode.com/problems/maximum-total-reward-using-operations-i/description/
    3181. Maximum Total Reward Using Operations II
        https://leetcode.com/problems/maximum-total-reward-using-operations-ii/description/
    """

    def numberOfChild(self, n: int, k: int) -> int:
        n -= 1
        rounds = k // n
        rem = k % n
        if rounds % 2 == 0:
            return rem
        else:
            return n - rem

    def valueAfterKSeconds(self, n: int, k: int) -> int:
        # pascal triangle
        MOD = 10**9 + 7
        return comb(k + n - 1, n - 1) % MOD

    def maxTotalReward(self, rewardValues: List[int]) -> int:
        # brute force with set
        rewardValues.sort()
        res = {0}
        for x in rewardValues:
            news = set()
            for y in res:
                if x > y:
                    news.add(x + y)
            res.update(news)
        return max(res)

    # with larger range constraints
    def maxTotalReward(self, rewards: List[int]) -> int:
        rewards = sorted(set(rewards))
        x, max_x = 1, (1 << rewards[-1]) - 1
        for reward in rewards:
            mask = (1 << reward) - 1
            x |= (x & mask) << reward & max_x
        return rewards[-1] + x.bit_length() - 1
