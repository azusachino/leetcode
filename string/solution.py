import collections


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        x, y = len(s), len(t)
        while i < x and j < y:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == x

    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split(" ")
        if len(pattern) != len(ss):
            return False
        x, y = {}, {}
        # for i in range(len(pattern)):
        #     if pattern[i] not in x:
        #         if ss[i] in y and y[ss[i]] != pattern[i]:
        #             return False
        #         x[pattern[i]] = ss[i]
        #         y[ss[i]] = pattern[i]
        #     else:
        #         if ss[i] not in y or y[ss[i]] != pattern[i]:
        #             return False
        for char, word in zip(pattern, ss):
            if (char in x and x[char] != word) or (word in y and y[word] != char):
                return False
            x[char] = word
            y[word] = char
        return True

    def customSortString(self, order: str, s: str) -> str:
        ret = ""
        c = collections.Counter(s)
        for o in order:
            if o in c:
                ret += o * c[o]
                # del c[o]
                c[o] = 0
        # not_in_order = ""
        # for k, v in c.items():
        #     not_in_order += k * v
        # return ret + not_in_order
        for n in s:
            if c[n]:
                ret += n
        return ret


if __name__ == "__main__":
    solution = Solution()
    s = "ace"
    t = "ahbegdc"
    r = solution.isSubsequence(s, t)
    print("isSubsequence", r)
