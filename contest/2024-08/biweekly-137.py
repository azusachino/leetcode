from typing import List


class Solution:
    """
    08.17
    3254. Find the Power of K-Size Subarrays I
        https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/description/
    3255. Find the Power of K-Size Subarrays II
        https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/description/
    3256. Maximum Value Sum by Placing Three Rooks I
        https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/
    3257. Maximum Value Sum by Placing Three Rooks II
        https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/
    """

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # n <= 500
        res = []
        for i in range(k - 1, len(nums)):
            x = nums[i]
            if res and res[-1] != -1 and res[-1] < x:
                res.append(x)
            else:
                sort = True
                for j in range(i - 1, i - k, -1):
                    # reverse order or not consecutive
                    if x <= nums[j] or x != nums[j] + 1:
                        res.append(-1)
                        sort = False
                        break
                    x = nums[j]
                if sort:
                    res.append(nums[i])
        return res

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # n <= 10**5
        res = []
        counts = 0
        for i in range(len(nums)):
            if i and nums[i] == nums[i - 1] + 1:
                counts += 1
            else:
                counts = 1
            if i + 1 >= k:
                if counts >= k:
                    res.append(nums[i])
                else:
                    res.append(-1)
        return res
