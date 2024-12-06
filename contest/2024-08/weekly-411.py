from itertools import accumulate
from typing import Counter, List


class Solution:
    """
    08.18
    3258. Count Substrings That Satisfy K-Constraint I
        https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/description/
    3259. Maximum Energy Boost From Two Drinks
        https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/description/
    3260. Find the Largest Palindrome Divisible by K
        https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/
    3261. Count Substrings That Satisfy K-Constraint II
        https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/
    """

    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = 0
        ones = 0
        l = 0
        for r, ch in enumerate(s):
            if ch == "1":
                ones += 1
            # one count or zero count overflow
            while ones > k and r - l - ones + 1 > k:
                if s[l] == "1":
                    ones -= 1
                l += 1
            res += r - l + 1
        return res

    def maxEnergyBoost(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        a = b = 0
        for i in range(n):
            a, b = max(a + A[i], b), max(b + B[i], a)
        return max(a, b)

    def largestPalindrome(self, n: int, k: int) -> str:
        # basic idea version

        def is_p(x):
            x = str(x)
            l, r = 0, len(x) - 1
            while l != r:
                if x[l] != x[r]:
                    return False
                l += 1
                r -= 1
            return True

        x = 10**n
        while x > k:
            if x % k == 0:
                if is_p(x):
                    return str(x)
            x -= 1
        return str(k)

    def largestPalindrome(self, n: int, k: int) -> str:
        # @credit https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/solutions/5653160/math-check-divisibility-rules-for-each-number-of-1-9/
        if k == 1:
            return "9" * n
        elif k == 2:
            if n <= 2:
                return "8" * n
            else:
                return "8" + "9" * (n - 2) + "8"
        elif k == 3 or k == 9:
            return "9" * n
        elif k == 4:
            if n <= 4:
                return "8" * n
            else:
                return "88" + "9" * (n - 4) + "88"
        elif k == 5:
            if n <= 2:
                return "5" * n
            else:
                return "5" + "9" * (n - 2) + "5"
        elif k == 6:
            if n <= 2:
                return "6" * n
            elif n % 2 == 1:
                l = n // 2 - 1
                return "8" + "9" * l + "8" + "9" * l + "8"
            else:
                l = n // 2 - 2
                return "8" + "9" * l + "77" + "9" * l + "8"
        elif k == 8:
            if n <= 6:
                return "8" * n
            else:
                return "888" + "9" * (n - 6) + "888"
        else:
            dic = {
                0: "",
                1: "7",
                2: "77",
                3: "959",
                4: "9779",
                5: "99799",
                6: "999999",
                7: "9994999",
                8: "99944999",
                9: "999969999",
                10: "9999449999",
                11: "99999499999",
            }
            l, r = divmod(n, 12)
            return "999999" * l + dic[r] + "999999" * l

    def countKConstraintSubstrings(
        self, s: str, k: int, queries: List[List[int]]
    ) -> List[int]:
        # @credit https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/solutions/5653148/o-n-sliding-window/
        counts = Counter()
        left = 0
        n = len(s)
        left_to_right = [0] * n
        right_to_left = [0] * n

        # For each right, find the minimum left
        for right in range(n):
            counts[s[right]] += 1
            while counts["0"] > k and counts["1"] > k:
                counts[s[left]] -= 1
                left += 1
            right_to_left[right] = left

        # For each left, find the maximum right
        right = n - 1
        counts = Counter()
        for left in reversed(range(n)):
            counts[s[left]] += 1
            while counts["0"] > k and counts["1"] > k:
                counts[s[right]] -= 1
                right -= 1
            left_to_right[left] = right

        # For the right indexes that has left within the query bounds, all the substrings count
        # For the right indexes that has left outside the query bounds, only substrings within the bounds will count
        # So, seperate the cases for each query

        pref_sum = [0] + list(
            accumulate([(right - left + 1) for right, left in enumerate(right_to_left)])
        )
        result = []
        for left_bound, right_bound in queries:
            middle = min(right_bound, left_to_right[left_bound])
            length = middle - left_bound + 1
            curr = length * (length + 1) // 2
            curr += (
                pref_sum[right_bound + 1] - pref_sum[middle + 1]
            )  # where left is within, so all the substrings count
            result.append(curr)
        return result
