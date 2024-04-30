import bisect
import collections
import itertools
import random
from typing import List


class Solution:
    """
    1154. Day of the Year
        https://leetcode.com/problems/day-of-the-year/description/
    1155. Number of Dice Rolls With Target Sum
        https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
        DP, memorization
    1156. Swap For Longest Repeated Character Substring
        https://leetcode.com/problems/swap-for-longest-repeated-character-substring/description/
    1157. Online Majority Element In Subarray
        https://leetcode.com/problems/online-majority-element-in-subarray/description/
    """

    def dayOfYear(self, date: str) -> int:
        from datetime import datetime

        y, m, d = map(int, date.split("-"))
        return (datetime(y, m, d) - datetime(y, 1, 1)).days + 1

    memo = {}
    mod = 10**9 + 7

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if (n, k, target) in self.memo:
            return self.memo[(n, k, target)]
        # the left is not enough
        if target < n or target > n * k:
            return 0
        # sum to target
        if n == 0:
            return 1 if target == 0 else 0
        self.memo[(n, k, target)] = (
            sum(self.numRollsToTarget(n - 1, k, target - x) for x in range(1, k + 1))
            % self.mod
        )
        return self.memo[(n, k, target)]

    def maxRepOpt1(self, S):
        # We get the group's key and length first, e.g. 'aaabaaa' -> [[a , 3], [b, 1], [a, 3]
        A = [[c, len(list(g))] for c, g in itertools.groupby(S)]
        # We also generate a count dict for easy look up e.g. 'aaabaaa' -> {a: 6, b: 1}
        count = collections.Counter(S)
        # only extend 1 more, use min here to avoid the case that there's no extra char to extend
        res = max(min(k + 1, count[c]) for c, k in A)
        # merge 2 groups together
        for i in range(1, len(A) - 1):
            # if both sides have the same char and are separated by only 1 char
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                # min here serves the same purpose
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
        return res


class MajorityChecker:
    """
    For each a in A, save its index of occurrence to list a2i[a].
    When we want to get the exact occurrence of a in a range,
    we can use binary search in a2i[a].

    In the general good cases,
    the numbers in A should be various,
    each number should appear 1 time in average,
    making the time complexity only O(1).

    In the specific worst cases to this binary search solution,
    the cases will be something like [1,2,1,2,1,2,1,2....],
    making the binary search O(logN), (search in a list of length N / 2).

    Now the only problem we need to solve,
    is that how to find the majority element if it exists.
    """

    def __init__(self, A):
        a2i = collections.defaultdict(list)
        for i, x in enumerate(A):
            a2i[x].append(i)
        self.A, self.a2i = A, a2i

    def query(self, left, right, threshold):
        for _ in range(20):
            a = self.A[random.randint(left, right)]
            l = bisect.bisect_left(self.a2i[a], left)
            r = bisect.bisect_right(self.a2i[a], right)
            if r - l >= threshold:
                return a
        return -1
