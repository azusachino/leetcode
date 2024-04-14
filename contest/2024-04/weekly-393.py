from typing import List


class Solution:
    """
    3114. Latest Time You Can Obtain After Replacing Characters
    3115. Maximum Prime Difference
    3116. Kth Smallest Amount With Single Denomination Combination
    3117. Minimum Sum of Values by Dividing Array
    """

    def findLatestTime(self, s: str) -> str:
        s = list(s)
        if s[0] == "?":
            s[0] = "1" if s[1] == "?" or s[1] <= "1" else "0"
        if s[1] == "?":
            s[1] = "1" if s[0] == "1" else "9"
        if s[3] == "?":
            s[3] = "5"
        if s[4] == "?":
            s[4] = "9"
        return "".join(s)

    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(num):
            """
            This function checks if a number is prime.

            Args:
              num: The number to check.

            Returns:
              True if the number is prime, False otherwise.
            """
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True

        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            x, y = is_prime(nums[l]), is_prime(nums[r])
            if x and y:
                return r - l
            elif x:
                r -= 1
            else:
                l += 1
        return 0

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        pass

    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        pass
