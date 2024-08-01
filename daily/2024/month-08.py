from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        """
        08.01
        2678. Number of Senior Citizens
        https://leetcode.com/problems/number-of-senior-citizens/description/
        """
        res = 0
        for d in details:
            age = int(d[11:13])
            if age > 60:
                res += 1
        return res
