import bisect
from typing import Counter, List


class Solution:
    """
    1232. Check If It Is a Straight Line
        https://leetcode.com/problems/check-if-it-is-a-straight-line/description/
    1233. Remove Sub-Folders from the Filesystem
        https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/
    1234. Replace the Substring for Balanced String
        https://leetcode.com/problems/replace-the-substring-for-balanced-string/
    1235. Maximum Profit in Job Scheduling
        https://leetcode.com/problems/maximum-profit-in-job-scheduling/
    """

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[:2]
        return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # sort folder in alphabet & length order
        folder.sort()
        ans = [folder[0]]
        for f in folder[1:]:
            m, n = len(ans[-1]), len(f)
            # current folder is sub-folder of previous
            if m < n and (ans[-1] == f[:m] and f[m] == "/"):
                continue
            else:
                ans.append(f)
        return ans

    def balancedString(self, s):
        count = Counter(s)
        res = n = len(s)
        i = 0
        for j, c in enumerate(s):
            count[c] -= 1
            while i < n and all(n / 4 >= count[c] for c in "QWER"):
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1
        return res

    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]
