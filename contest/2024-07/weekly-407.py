from itertools import pairwise
from typing import List


class Solution:
    """
    2027.07.21
    3226. Number of Bit Changes to Make Two Integers Equal
        https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/description/
    3227. Vowels Game in a String
        https://leetcode.com/problems/vowels-game-in-a-string/
    3228. Maximum Number of Operations to Move Ones to the End
        https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/
    3229. Minimum Operations to Make Array Equal to Target
        https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/description/
    bonus:
    1526. Minimum Number of Increments on Subarrays to Form a Target Array
        https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/description/
    """

    def minChanges(self, n: int, k: int) -> int:
        """
        def minChanges(self, n: int, k: int) -> int:
            result = 0
            current = 1
            while current <= n or current <= k:
                bit_n = n & current
                bit_k = k & current
                if bit_n > bit_k:
                    result += 1
                if bit_n < bit_k:
                    return -1
                current *= 2
            return result
        """
        if n < k:
            return -1
        if n == k:
            return 0
        x, y = str(bin(n)), str(bin(k))
        res = 0
        for i in range(len(y)):
            if y[-i] == "b":
                break
            if x[-i] == "0" and y[-i] == "1":
                return -1
            elif x[-i] == "1" and y[-i] == "0":
                res += 1
        for j in range(i, len(x)):
            if x[-j] == "b":
                break
            if x[-j] == "1":
                res += 1
        return res

    def doesAliceWin(self, s: str) -> bool:
        """
        If the number of vowels is 0, Bob wins because Alice has no vowels to pick.
        If the number of vowels is odd, Alice can pick all of them on her turn. In this case, Bob will have no vowels left to pick on his turn, resulting in Bob losing.
        If the number of vowels is even, say n, Alice can pick n - 1 vowels on her turn, leaving exactly 1 vowel (which is odd) for Bob. Bob will then be unable to pick any more vowels on his turn, resulting in Bob losing.
        Therefore, if the count of vowels is greater than 0, Alice will win; otherwise, Bob will win.
        """
        vowels = set("aeiou")
        return any(c in vowels for c in s)

    def maxOperations(self, s: str) -> int:
        cnt_one = 0
        res = 0
        prev = None
        for c in s:
            if c == "1":
                cnt_one += 1
            elif c == "0" and prev == "1":
                res += cnt_one
            prev = c
        return res

    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        # @credit https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/solutions/5509031/java-c-python-just-sum-up-increments/
        arr = [y - x for x, y in zip(nums, target)]
        return sum(max(y - x, 0) for x, y in pairwise([0] + arr + [0]))

    def minNumberOperations(self, target: List[int]) -> int:
        return sum(max(y - x, 0) for x, y in pairwise([0] + target + [0]))

    def minNumberOperations(self, target: List[int]) -> int:
        res = pre = 0
        for i in target:
            # calculate all the incremental
            res += max(0, i - pre)
            pre = i
        return res + max(0, -pre)
