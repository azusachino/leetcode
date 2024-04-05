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

    def minimumDeletions(self, word: str, k: int) -> int:
        """
        1. calculate character frequencies
        2. delete characters for two reasons
            2.1 delete the small frequency to zero, so it doesn't count for the rule
            2.2 delete the big frequency smaller, so it `big freq - small freq <= k`
                and don't reduce small freq to smaller positive
        """
        freq = collections.Counter(word).values()
        # in worst case, delete all
        res = len(word)
        for a in freq:
            cur = 0
            for b in freq:
                if b < a:
                    cur += b
                else:
                    cur += max(0, b - (a + k))
            res = min(res, cur)
        return res

    def isSubstringPresent(self, s: str) -> bool:
        mp = collections.defaultdict(set)
        n = len(s)
        for i in range(1, n):
            mp[s[i - 1]].add(s[i])
        for i in range(1, n):
            if s[i - 1] in mp[s[i]]:
                return True
        return False

    def maximumLengthSubstring(self, s: str) -> int:
        window = collections.defaultdict(int)
        l = r = 0
        ret = 0
        while r < len(s):
            window[s[r]] += 1
            r += 1
            max_freq = max(window.values())
            if max_freq <= 2:
                ret = max(ret, r - l)
            else:
                window[s[l]] -= 1
                l += 1
        return ret

    def maxDepth(self, s: str) -> int:
        res = cur = 0
        for c in s:
            # constraint guaranteed validity
            if c == "(":
                cur += 1
                res = max(res, cur)
            elif c == ")":
                cur -= 1
        return res

    def convert(self, s: str, numRows: int) -> str:
        rows, idx = [""] * numRows, 0
        # 0 or -1
        step = (numRows == 1) - 1
        for c in s:
            rows[idx] += c
            if idx == 0 or idx == numRows - 1:
                step = -step
            idx += step
        return "".join(rows)

    def sortVowels(self, s: str) -> str:
        vowels = set(["a", "e", "u", "i", "o", "A", "E", "U", "I", "O"])
        loc = [0] * len(s)
        srt = []
        for i, c in enumerate(s):
            if c in vowels:
                loc[i] = 1
                srt.append(c)
        srt.sort()
        idx = 0
        ss = list(s)
        for i, c in enumerate(loc):
            if c:
                ss[i] = srt[idx]
                idx += 1
        return "".join(ss)


if __name__ == "__main__":
    solution = Solution()
    s = "ace"
    t = "ahbegdc"
    r = solution.isSubsequence(s, t)
    print("isSubsequence", r)
    string = "adaddccdb"
    n = len(string)
    print(solution.maximumLengthSubstring(string))
    s_ = "PAYPALISHIRING"
    print(solution.convert(s_, 3))
