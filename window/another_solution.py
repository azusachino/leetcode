from collections import Counter


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

    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        n = len(s)
        # impossible to form 26+1 or n+1 distinct characters
        if k > 26 or k > n:
            return 0
        res = 0
        cnt = Counter()
        l = 0
        for r in range(n):
            cnt[s[r]] += 1
            while cnt[s[r]] > 1 or r - l + 1 > k:
                cnt[s[l]] -= 1
                l += 1
            res += r - l + 1 == k
        return res


if __name__ == "__main__":
    solution = Solution()
    s = "havefunonleetcode"
    print(solution.numKLenSubstrNoRepeats(s, 5))
