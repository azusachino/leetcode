import math
from typing import List


class Solution:
    """
    2024.07.28
    3232. Find if Digit Game Can Be Won
        https://leetcode.com/problems/find-if-digit-game-can-be-won/description/
    3233. Find the Count of Numbers Which Are Not Special
        https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/description/
    3234. Count the Number of Substrings With Dominant Ones
        https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/description/
    3235. Check if the Rectangle Corner Is Reachable
        https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/description/
    """

    def canAliceWin(self, nums: List[int]) -> bool:
        sum_of_digit = sum(x if x < 10 else 0 for x in nums)
        return not sum(nums) == 2 * sum_of_digit

    def nonSpecialCount(self, l: int, r: int) -> int:
        # Calculate the limit up to which we need to find prime numbers
        lim = int(math.sqrt(r))

        # Create a list to mark primes up to lim using Sieve of Eratosthenes
        is_prime = [True] * (lim + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

        # Sieve of Eratosthenes to mark non-prime numbers
        for i in range(2, int(math.sqrt(lim)) + 1):
            if is_prime[i]:
                for j in range(i * i, lim + 1, i):
                    is_prime[j] = False

        # Count special numbers in the range [l, r]
        special_count = 0
        for i in range(2, lim + 1):
            if is_prime[i]:
                square = i * i
                if l <= square <= r:
                    special_count += 1

        # Total numbers in the range [l, r]
        total_count = r - l + 1

        # Calculate non-special numbers
        return total_count - special_count

    def numberOfSubstrings(self, s: str) -> int:
        # @credit https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/solutions/5546329/easy-sliding-window-detailed-explanation-o-nsqrtn/
        n = len(s)
        ans = 0
        for z in range(math.isqrt(n) + 1):
            j = zeroj = 0
            k = zerok = onek = 0
            for i, ch in enumerate(s):
                if ch == "0":
                    zeroj += 1
                    zerok += 1
                else:
                    onek += 1
                while zeroj > z:
                    if s[j] == "0":
                        zeroj -= 1
                    j += 1
                while zerok > z or k <= i and zerok == z and onek >= zerok**2:
                    if s[k] == "0":
                        zerok -= 1
                    else:
                        onek -= 1
                    k += 1
                ans += k - j
        return ans

    def canReachCorner(self, X: int, Y: int, A: List[List[int]]) -> bool:
        # @credit https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/solutions/5546344/python-union-find/
        def find(i):
            if f[i] != i:
                f[i] = find(f[i])
            return f[i]

        n = len(A)
        f = list(range(n + 2))
        for i in range(n):
            x, y, r = A[i]
            if x - r <= 0 or y + r >= Y:
                f[find(n)] = find(i)
            if x + r >= X or y - r <= 0:
                f[find(n + 1)] = find(i)
            for j in range(i):
                x2, y2, r2 = A[j]
                if (x - x2) ** 2 + (y - y2) ** 2 <= (r + r2) ** 2:
                    f[find(i)] = find(j)
        return find(n) != find(n + 1)
