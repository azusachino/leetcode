from typing import List


class Solution:
    """
    1221. Split a String in Balanced Strings
        https://leetcode.com/problems/split-a-string-in-balanced-strings/description/
        string
    1222. Queens That Can Attack the King
        https://leetcode.com/problems/queens-that-can-attack-the-king/description/
    1223. Dice Roll Simulation
        https://leetcode.com/problems/dice-roll-simulation/description/
    1224. Maximum Equal Frequency
        https://leetcode.com/problems/maximum-equal-frequency/
    """

    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        l = r = 0
        for c in s:
            if c == "L":
                l += 1
            else:
                r += 1
            if l and r and l == r:
                cnt += 1
                l = r = 0
        return cnt

    def queensAttacktheKing(
        self, queens: List[List[int]], king: List[int]
    ) -> List[List[int]]:
        n = 8
        # queen set
        s = {(i, j) for i, j in queens}
        ans = []
        # eight directions
        for a in range(-1, 2):
            for b in range(-1, 2):
                if a or b:
                    x, y = king
                    while 0 <= x + a < n and 0 <= y + b < n:
                        x, y = x + a, y + b
                        if (x, y) in s:
                            ans.append([x, y])
                            break
        return ans
