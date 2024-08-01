from typing import List


class Solution:
    """
    1662. Check If Two String Arrays are Equivalent
        https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/
    1663. Smallest String With A Given Numeric Value
        https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/description/
    1664. Ways to Make a Fair Array
        https://leetcode.com/problems/ways-to-make-a-fair-array/
    1665. Minimum Initial Energy to Finish Tasks
        https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/description/
    """

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # much slower than fail fast
        return "".join(word1) == "".join(word2)

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def chars(word):
            for segment in word:
                for char in segment:
                    yield char
            yield None

        return all(c1 == c2 for c1, c2 in zip(chars(word1), chars(word2)))

    def getSmallestString(self, n: int, k: int) -> str:
        res = ["a"] * n
        k -= n
        a = ord("a")
        while k > 0:
            n -= 1
            res[n] = chr(a + min(k, 25))
            k -= min(25, k)

        return "".join(res)

    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        odd_prefix, even_prefix = [0] * (n + 1), [0] * (n + 1)
        for i, num in enumerate(nums):
            # [2,1,6,4]
            # [2, 2, 8, 8, 0] [0, 1, 1, 5, 0]
            odd_prefix[i] += odd_prefix[i - 1]
            even_prefix[i] += even_prefix[i - 1]
            if i % 2 == 0:
                even_prefix[i] += num
            else:
                odd_prefix[i] += num
        result = 0
        for i, num in enumerate(nums):
            even_after_removed = even_prefix[i - 1] + odd_prefix[n - 1] - odd_prefix[i]
            odd_after_removed = odd_prefix[i - 1] + even_prefix[n - 1] - even_prefix[i]
            result += even_after_removed == odd_after_removed
        return result

    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # We want to go through tasks in descending order of energy we could carry
        # over to the next task
        tasks.sort(key=lambda x: -(x[1] - x[0]))

        curr_energy = 0
        borrowed = 0
        for i in range(len(tasks)):
            need = max(0, max(tasks[i]) - curr_energy)
            borrowed += need
            curr_energy = curr_energy + need - tasks[i][0]

        return borrowed
