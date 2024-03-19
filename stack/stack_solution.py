from typing import List


class Solution:

    def isValid(self, s: str) -> bool:
        d = {")": "(", "]": "[", "}": "{"}
        stk = []
        for c in s:
            if c in d:
                if not stk or stk.pop() != d[c]:
                    return False
            else:
                stk.append(c)
        return not stk

    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stk = []
        for p in paths:
            if not p or p == ".":
                continue
            if p != "..":
                stk.append(p)
            elif stk:
                stk.pop()

        r = ""
        for p in stk:
            r += "/" + p
        if r:
            return r
        return "/"

    def asteroidCollision(self, nums: List[int]) -> List[int]:
        stk = []
        for n in nums:
            while stk and n < 0 and stk[-1] > 0:
                bang = stk[-1] + n
                # in stack positive, crashed
                if bang <= 0:
                    stk.pop()
                # in flight negative, crashed
                if bang >= 0:
                    break
            else:
                stk.append(n)
        return stk


if __name__ == "__main__":
    solution = Solution()
    s = "()[]{})"
    r = solution.isValid(s)
    print("isValid", r)
    # path = "/home//foo/"
    # r = solution.simplifyPath(path)
    # print("simplifyPath", r)
