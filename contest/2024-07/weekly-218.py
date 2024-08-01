from collections import Counter
from itertools import combinations, permutations
from typing import List


class Solution:
    """
    1678. Goal Parser Interpretation
        https://leetcode.com/problems/goal-parser-interpretation/description/
    1679. Max Number of K-Sum Pairs
        https://leetcode.com/problems/max-number-of-k-sum-pairs/description/
    1680. Concatenation of Consecutive Binary Numbers
        https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/description/
    1681. Minimum Incompatibility
        https://leetcode.com/problems/minimum-incompatibility/description/
    """

    def interpret(self, command: str) -> str:
        """
        public String interpret(String command) {
            StringBuilder S = new StringBuilder(command.length());
            for(int i = 0 ; i < command.length() ; i++){
                if(command.charAt(i)=='G') S.append('G');
                if(command.charAt(i)=='('){
                    if(command.charAt(i+1)==')') {S.append('o'); i++;}
                    else{S.append("al"); i = i + 3;}
                }
            }
            return S.toString();
        }
        """
        return command.replace("()", "o").replace("(al)", "al")

    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        res = 0
        # calculated twice
        for val in cnt:
            res += min(cnt[val], cnt[k - val])
        # divide 2
        return res // 2

    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        res = 0
        for i in range(1, n + 1):
            res = (res << i.bit_length() | i) & mod
        return res

    def minimumIncompatibility(self, nums, k):
        """
        @credit https://leetcode.com/problems/minimum-incompatibility/solutions/961969/python-true-o-n-n-2-n-bit-dp-explained/
        """
        n = len(nums)
        if k == n:
            return 0
        dp = [[float("inf")] * n for _ in range(1 << n)]
        nums.sort()
        for i in range(n):
            dp[1 << i][i] = 0

        for mask in range(1 << n):
            n_z_bits = [j for j in range(n) if mask & (1 << j)]
            if len(n_z_bits) % (n // k) == 1:
                for j, l in permutations(n_z_bits, 2):
                    dp[mask][l] = min(dp[mask][l], dp[mask ^ (1 << l)][j])
            else:
                for j, l in combinations(n_z_bits, 2):
                    if nums[j] != nums[l]:
                        dp[mask][j] = min(
                            dp[mask][j], dp[mask ^ (1 << j)][l] + nums[l] - nums[j]
                        )

        return min(dp[-1]) if min(dp[-1]) != float("inf") else -1
