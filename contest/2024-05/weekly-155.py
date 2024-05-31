from collections import defaultdict
from itertools import pairwise
from math import lcm
from typing import List


class Solution:
    """
    1200. Minimum Absolute Difference
        https://leetcode.com/problems/minimum-absolute-difference/
    1201. Ugly Number III
        https://leetcode.com/problems/ugly-number-iii/
    1202. Smallest String With Swaps
        https://leetcode.com/problems/smallest-string-with-swaps/description/
    1203. Sort Items by Groups Respecting Dependencies
        https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/description/
    """

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mi = min(b - a for a, b in pairwise(arr))
        return [[a, b] for a, b in pairwise(arr) if b - a == mi]

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(a, b, c)
        l, r = 1, 2 * 10**9
        while l < r:
            mid = (l + r) >> 1
            if (
                mid // a
                + mid // b
                + mid // c
                - mid // ab
                - mid // bc
                - mid // ac
                + mid // abc
                >= n
            ):
                r = mid
            else:
                l = mid + 1
        return l

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        the index pairs have transitivity, i.e., if a and b can be swapped, and b and c can be swapped, then a and c can also be swapped. Therefore, we can consider using a union-find data structure to maintain the connectivity of these index pairs, and sort the characters belonging to the same connected component in lexicographical order.

        Finally, we traverse the string. For the character at the current position, we replace it with the smallest character in the connected component, then remove this character from the connected component, and continue to traverse the string.
        """

        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        n = len(s)
        p = list(range(n))
        for a, b in pairs:
            p[find(a)] = find(b)
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[find(i)].append(c)
        for i in d.keys():
            d[i].sort(reverse=True)
        return "".join(d[find(i)].pop() for i in range(n))

    def sortItems(
        self, n: int, m: int, group: List[int], beforeItems: List[List[int]]
    ) -> List[int]:
        pass


def gcd(a: int, b: int) -> int:
    if not b:
        return a
    return gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)
