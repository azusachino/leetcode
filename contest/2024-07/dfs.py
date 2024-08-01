import operator
from typing import List


class Solution:
    """
    241. Different Ways to Add Parentheses
        https://leetcode.com/problems/different-ways-to-add-parentheses/description/
    """

    def diffWaysToCompute(self, expression: str) -> List[int]:
        op_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
        }

        def dfs(start, end):
            res = []
            for i in range(start, end + 1):
                c = expression[i]
                # operand
                if c in "+-*":
                    ls = dfs(start, i - 1)
                    rs = dfs(i + 1, end)
                    for l in ls:
                        for r in rs:
                            res.append(op_map[c](l, r))
            return res or [int(expression[start : end + 1])]

        return dfs(0, len(expression) - 1)
