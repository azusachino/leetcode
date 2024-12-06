class Solution:
    """
    11.03 https://leetcode.com/contest/weekly-contest-422/
    3340. Check Balanced String
        https://leetcode.com/problems/check-balanced-string/description/
    """

    def isBalanced(self, num: str) -> bool:
        num = int(num)
        x = y = 0
        ok = True
        while num:
            tmp = num % 10
            num //= 10
            if ok:
                x += tmp
            else:
                y += tmp
            ok = not ok
        return x == y
