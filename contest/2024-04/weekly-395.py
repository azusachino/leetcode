import heapq
from typing import Counter, List


class Solution:
    """
    3131. Find the Integer Added to Array I
        https://leetcode.com/problems/find-the-integer-added-to-array-i/description/
    3132. Find the Integer Added to Array II
        https://leetcode.com/problems/find-the-integer-added-to-array-ii/
    3133. Minimum Array End
        https://leetcode.com/problems/minimum-array-end/description/
    3134. Find the Median of the Uniqueness Array
        https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/description/
    """

    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return sorted(nums2)[0] - sorted(nums1)[0]

    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        min2 = min(nums2)
        c, b, a = [min2 - val for val in heapq.nsmallest(3, nums1)]
        nums2 = Counter(nums2)
        for x in (a, b, c):
            if nums2 <= Counter(val + x for val in nums1):
                return x

    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        b = 1
        for _ in range(64):
            if b & x == 0:
                x |= (n & 1) * b
                n >>= 1
            b <<= 1
        return x

    def medianOfUniquenessArray(self, A: List[int]) -> int:
        """
        Sliding Window + Binary Search
        """
        n = len(A)
        total = n * (n + 1) // 2

        def atmost(k):
            res = 0
            count = Counter()
            i = 0
            for j in range(n):
                count[A[j]] += 1
                while len(count) > k:
                    count[A[i]] -= 1
                    if count[A[i]] == 0:
                        del count[A[i]]
                    i += 1
                res += j - i + 1
            return res

        left, right = 1, len(set(A))
        while left < right:
            k = (left + right) // 2
            if atmost(k) * 2 >= total:
                right = k
            else:
                left = k + 1
        return left
