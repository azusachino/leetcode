from collections import Counter
from typing import List, Optional

from tree.local_tree import TreeNode


class Solution:
    """
    1118. Number of Days in a Month
    1119. Remove Vowels from a String
    1120. Maximum Average Subtree
    1121. Divide Array Into Increasing Sequences
    """

    def numberOfDays(self, year: int, month: int) -> int:
        """
        Input: year = 1992, month = 7
        Output: 31
        Input: year = 2000, month = 2
        Output: 29
        """
        # If the year can be divided by but not by, or can be divided by, then this year is a leap year.
        leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        days = [0, 31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days[month]

    def removeVowels(self, s: str) -> str:
        """
        Input: s = "leetcodeisacommunityforcoders"
        Output: "ltcdscmmntyfrcdrs"
        """
        st = set(list("aeiou"))
        return "".join(c for c in s if c not in st)

    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        """
        Input: root = [5,6,1]
        Output: 6.00000
        """
        self.res = 0

        def dfs(node):
            if not node:
                return 0, 0
            # track sum of count
            ls, ln = dfs(node.left)
            rs, rn = dfs(node.right)
            s = node.val + ls + rs
            n = 1 + ln + rn
            # update result for each root
            self.res = max(self.res, s // n)
            return s, n

        dfs(root)
        return self.res

    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        """
        Input: nums = [1,2,2,3,3,4,4], k = 3
        Output: true
        Explanation: The array can be divided into two subsequences [1,2,3,4] and [2,3,4] with lengths at least 3 each.
        """
        count = Counter(nums)
        # impossible to divide into k groups without duplicates
        groups = max(count.values())
        return len(nums) >= k * groups


if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfDays(1900, 2))
    print(solution.removeVowels("leetcodeisacommunityforcoders") == "ltcdscmmntyfrcdrs")
