from math import inf
from typing import List
from collections import Counter


class Solution:
    """
    09.15
    3289. The Two Sneaky Numbers of Digitville
        https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/
    3290. Maximum Multiplication Score
        https://leetcode.com/problems/maximum-multiplication-score/description/
    3291. Minimum Number of Valid Strings to Form Target I
        https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/description/
    3292. Minimum Number of Valid Strings to Form Target II
        https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/description/
    """

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        res = []
        for k, v in cnt.items():
            if v == 2:
                res.append(k)
        return res

    def maxScore(self, a: List[int], B: List[int]) -> int:
        """
        3290. Maximum Multiplication Score
        https://leetcode.com/problems/maximum-multiplication-score/description/
        """
        dp = [-inf] * 4 + [0]
        for b in B:
            for i in range(3, -1, -1):
                dp[i] = max(dp[i], dp[i - 1] + a[i] * b)
        return dp[3]

    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node["#"] = word
        n = len(target)
        dp = [inf] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            node = trie
            for j in range(i, n):
                if target[j] in node:
                    node = node[target[j]]
                else:
                    break
                dp[i] = min(dp[i], 1 + dp[j + 1])
        return dp[0] if dp[0] < inf else -1
