from typing import Counter, List


class Solution:
    """
    3162. Find the Number of Good Pairs I
        https://leetcode.com/problems/find-the-number-of-good-pairs-i/description/
    3163. String Compression III
        https://leetcode.com/problems/string-compression-iii/
    3164. Find the Number of Good Pairs II
        https://leetcode.com/problems/find-the-number-of-good-pairs-ii/description/
    3165. Maximum Sum of Subsequence With Non-adjacent Elements
        https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/description/
    """

    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnt = 0
        for x in nums1:
            for y in nums2:
                if x % (y * k) == 0:
                    cnt += 1

        return cnt

    def compressedString(self, word: str) -> str:
        cur = ""
        curc = 0
        res = ""
        for c in word:
            if cur != c:
                if curc:
                    res += str(curc) + cur
                cur = c
                curc = 1
            else:
                curc += 1
                if curc > 9:
                    res += "9" + cur
                    curc = 1
        if curc:
            res += str(curc) + cur
        return res

    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        freqs = Counter(num * k for num in nums2)
        counts = [0] * (max(nums1) + 1)

        for num, count in freqs.items():
            for multiplier in range(num, len(counts), num):
                counts[multiplier] += count

        return sum(counts[num] for num in nums1)
