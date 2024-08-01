import heapq
from typing import List


class Solution:
    """
    3168. Minimum Number of Chairs in a Waiting Room
        https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/description/
    3169. Count Days Without Meetings
        https://leetcode.com/problems/count-days-without-meetings/
    3170. Lexicographically Minimum String After Removing Stars
        https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/
    3171. Find Subarray With Bitwise OR Closest to K
        https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/
    """

    def minimumChairs(self, s: str) -> int:
        res = 0
        cur = 0
        for c in s:
            if c == "E":
                cur += 1
            else:
                cur = max(0, cur - 1)
            res = max(cur, res)
        return res

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        # merge
        new_m = []
        for cur in meetings:
            if not new_m:
                new_m.append(cur)
            else:
                if new_m[-1][1] >= cur[0]:
                    new_m[-1][1] = max(new_m[-1][1], cur[1])
                else:
                    new_m.append(cur)

        used = 0
        for x in new_m:
            used += x[1] - x[0] + 1
        return days - used

    def clearStars(self, s: str) -> str:
        st = []
        index = []
        for c in s:
            if c == "*":
                if not st:
                    continue
                else:
                    st[-heapq.heappop(index)[1]][1] = 0
            else:
                st.append([c, 1])
                heapq.heappush(index, [ord(c), -(len(st) - 1), c])
        res = ""
        for x in st:
            if x[1]:
                res += x[0]
        return res

    def minimumDifference(self, nums: List[int], k: int) -> int:
        pass
