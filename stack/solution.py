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


if __name__ == "__main__":
    solution = Solution()
    s = "()[]{})"
    r = solution.isValid(s)
    print("isValid", r)
    # path = "/home//foo/"
    # r = solution.simplifyPath(path)
    # print("simplifyPath", r)
