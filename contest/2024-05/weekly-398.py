from math import comb
from typing import Counter, List


class Solution:
    """
    3151. Special Array I
        https://leetcode.com/problems/special-array-i/description/
    3152. Special Array II
        https://leetcode.com/problems/special-array-ii/
    3153. Sum of Digit Differences of All Pairs
        https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/description/
    3154. Find Number of Ways to Reach the K-th Stair
        https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/
    """

    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i - 1] % 2 == nums[i] % 2:
                return False

        return True

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        """
        vector<bool> isArraySpecial(vector<int>& nums, vector<vector<int>>& queries) {
            vector<bool> ans;
            vector<int> converted(1, 0);
            for(int i = 1, j = 0; i < nums.size(); ++i){
                if( (nums[i]%2) == (nums[i-1]%2) ) j++;
                converted.push_back(j);
            }
            for(auto q: queries) ans.push_back( converted[q[0]] == converted[q[1]] );
            return ans;
        }
        """
        preSum = [1]
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                preSum.append(preSum[-1])
            else:
                preSum.append(preSum[-1] + 1)
        res = []
        for s, e in queries:
            if preSum[e] - preSum[s] == e - s:
                res.append(True)
            else:
                res.append(False)
        return res

    def sumDigitDifferences(self, ar: List[int]) -> int:
        ar = list(map(str, ar))
        n, m = len(ar), len(ar[0])
        cnt = Counter()
        # m,k combination count
        res = comb(n, 2) * m
        for s in ar:
            for i, d in enumerate(s):
                res -= cnt[i, d]
                cnt[i, d] += 1
        return res

    def waysToReachStair(self, k: int) -> int:
        pass
