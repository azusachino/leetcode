from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        to_check = [0] * (len(nums) + 1)
        for n in nums:
            to_check[n] = 1
        for i, to in enumerate(to_check):
            if to == 0:
                return i
        return -1


class AlternativeSolution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > mid:
                r = mid
            else:
                l = mid + 1
        return l


class AnotherSolution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        sum = n * (n + 1) // 2
        """
        nums_sum = 0
        n = len(nums)
        total = n * (n + 1) // 2
        for n in nums:
            nums_sum += n
        return total - nums_sum


if __name__ == "__main__":
    s = Solution()
    # nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    nums = [0, 1]
    print("v ", s.missingNumber(nums))
