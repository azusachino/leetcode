from typing import List


class Solution:
    """
    09.22
    3295. Report Spam Message
        https://leetcode.com/problems/report-spam-message/description/
    3296. Minimum Number of Seconds to Make Mountain Height Zero
        https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/description/
    3297. Count Substrings That Can Be Rearranged to Contain a String I
        https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/description/
    3298. Count Substrings That Can Be Rearranged to Contain a String II
        https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/description/
    """

    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bw = set(bannedWords)
        cnt = 0
        for x in message:
            if x in bw:
                cnt += 1
            if cnt >= 2:
                return True
        return False

    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        pass

    def validSubstringCount(self, word1: str, word2: str) -> int:
        pass
