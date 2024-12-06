from typing import List


class Solution:
    """
    10.20
    3324. Find the Sequence of Strings Appeared on the Screen
        https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/
    """
    def stringSequence(self, target: str) -> List[str]:
        res = []
        base = ord("a")
        prev = ""
        for c in target:
            cur = 0
            while cur != ord(c) - base + 1:
                res.append(prev + chr(cur + base))
                cur += 1
            prev += c
        return res
