class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        window = set()
        l = r = 0
        res = 0
        while r < n:
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res, (r - l) + 1)
            r += 1
        return res
